#!/usr/bin/python
# ex:ts=4:sw=4:sts=4:et
# -*- tab-width: 4; c-basic-offset: 4; indent-tabs-mode: nil -*-

# The unittest framwork doesn't play nice with pylint:
#   pylint: disable-msg=C0103

from __future__ import absolute_import
import unittest
from svtplay_dl.service.tests import HandlesURLsTestMixin
from svtplay_dl.service.expressen import Expressen


class handlesTest(unittest.TestCase, HandlesURLsTestMixin):
    service = Expressen
    urls = {
        "ok": [
            "http://www.expressen.se/tv/nyheter/kungligt/se-nar-estelle-stjal-kungens-show/",
        ],
        "bad": [
            "http://www.oppetarkiv.se/video/1129844/jacobs-stege-ep1",
            "http://www.dn.se/nyheter/sverige/det-ar-en-dodsfalla"
        ]
    }
