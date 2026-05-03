# Copyright (c) 2026 Julien Palard.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pathlib import Path
from subprocess import DEVNULL, run

from hypothesis import HealthCheck, given, settings
from hypothesis.strategies import binary, text


def isutf8(string: bytes) -> bool:
    """Basic implementation of isutf8 in Python."""
    try:
        string.decode("UTF-8")
        return True
    except UnicodeDecodeError:
        return False


@settings(max_examples=5_000)
@given(data=text())
def test_isutf8_str(data):
    result = run(["./isutf8"], input=data.encode("UTF-8"))
    assert result.returncode == 0


@settings(max_examples=5_000)
@given(data=binary())
def test_isutf8_bytes(data):
    result = run(["./isutf8"], input=data, stdout=DEVNULL, stderr=DEVNULL)

    if isutf8(data):
        assert result.returncode == 0
    else:
        assert result.returncode != 0
