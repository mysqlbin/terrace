#!/usr/bin/env python
import datetime
import json


class RewriteJsonEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super(RewriteJsonEncoder, self).default(z)

