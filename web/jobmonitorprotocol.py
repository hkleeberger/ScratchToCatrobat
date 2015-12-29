#  ScratchToCatrobat: A tool for converting Scratch projects into Catrobat programs.
#  Copyright (C) 2013-2015 The Catrobat Team
#  (<http://developer.catrobat.org/credits>)
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  An additional term exception under section 7 of the GNU Affero
#  General Public License, version 3, is available at
#  http://developer.catrobat.org/license_additional_term
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import json

CLIENT = "CLIENT"
SERVER = "SERVER"

_logger = logging.getLogger(__name__)

class Request(object):
    class Command(object):
        AUTH = "AUTH"
        JOB_STARTED_NOTIFICATION = "JOB_STARTED_NOTIFICATION"
        JOB_PROGRESS_NOTIFICATION = "JOB_PROGRESS_NOTIFICATION"
        JOB_FINISHED_NOTIFICATION = "JOB_FINISHED_NOTIFICATION"
        FILE_TRANSFER = "FILE_TRANSFER"

    CMD = "CMD"
    ARGS = "ARGS"

    ARGS_MSG = "ARGS_MSG"
    ARGS_PROGRESS = "ARGS_PROGRESS"
    ARGS_RESULT = "ARGS_RESULT"
    ARGS_AUTH_KEY = "ARGS_AUTH_KEY"
    ARGS_FILE_NAME = "ARGS_FILE_NAME"
    ARGS_FILE_SIZE = "ARGS_FILE_SIZE"
    ARGS_FILE_HASH = "ARGS_FILE_HASH"

    COMMAND_ARGS = {
        Command.AUTH: [ARGS_AUTH_KEY],
        Command.JOB_STARTED_NOTIFICATION: [ARGS_MSG],
        Command.JOB_PROGRESS_NOTIFICATION: [ARGS_PROGRESS, ARGS_MSG],
        Command.JOB_FINISHED_NOTIFICATION: [ARGS_RESULT, ARGS_MSG],
        Command.FILE_TRANSFER: [ARGS_FILE_NAME, ARGS_FILE_SIZE, ARGS_FILE_HASH]
    }

    def __init__(self, cmd, args=None):
        self.cmd = cmd
        self.args = args

    def bytedata(self):
        data = { self.__class__.CMD: self.cmd, self.__class__.ARGS: self.args }
        return (json.dumps(data)+"\n").encode()

    @classmethod
    def request_from_data(cls, data):
        return cls(data[cls.CMD], data[cls.ARGS])

    @classmethod
    def is_valid(cls, data, expected_cmd):
        if (data != None) and (cls.CMD in data) or (cls.ARGS in data):
            for arg in cls.COMMAND_ARGS[expected_cmd]:
                if arg not in data[cls.ARGS]:
                    return False
            return True
        return False

class Reply(object):
    KEY_RESULT = "RESULT"
    KEY_MSG = "MSG"

    def __init__(self, result, msg):
        self.result = result
        self.msg = msg

    def bytedata(self):
        return (json.dumps({
            self.__class__.KEY_RESULT: self.result,
            self.__class__.KEY_MSG: self.msg
        })+"\n").encode()

    @classmethod
    def is_valid(cls, data):
        return (data is not None) and (cls.KEY_RESULT in data) and (cls.KEY_MSG in data)

class TCPConnection(object):
    def __init__(self, stream, address, counterpart=CLIENT, on_close_callback=None):
        self.stream = stream
        self.address = address
        self.stream.set_close_callback(self.on_close)
        self._me = CLIENT if counterpart == SERVER else SERVER
        self._counterpart = counterpart
        self.on_close_callback = on_close_callback
        _logger.info('Opened new connection from "%s"' % str(address))

    def read_message(self):
        return self.stream.read_until(b'\n')

    def send_message(self, data, logging_enabled=True):
        if self.stream.closed():
            return None
        if not isinstance(data, (Request, Reply)):
            if logging_enabled:
                _logger.debug("[%s]: %s" % (self._me, data))
            return self.stream.write(data)
        data = data.bytedata()
        if logging_enabled:
            _logger.debug("[%s]: %s" % (self._me, str(data).rstrip()))
        return self.stream.write(data)

    def on_close(self):
        _logger.info('Closed connection to %s' % str(self.address))
        if self.on_close_callback != None:
            self.on_close_callback()

    def print_error_and_close_stream(self):
        if not self.stream.closed():
            _logger.error("[%s]: An error occured: Stream will be closed!" % self._me)
            self.stream.close()
        else:
            _logger.error("[%s] An error occured: Stream has been closed!" % self._me)