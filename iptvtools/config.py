#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.py
Author: huxuan
Email: i(at)huxuan.org
Description: Configuration for iptvtools.
"""
import json
import os
import os.path


class Config():
    """Configuration for iptvtools."""
    config = {}

    @classmethod
    def init(cls, config_file):
        """Initialize configuration."""
        if os.path.isfile(config_file):
            with open(config_file) as fin:
                cls.config = json.load(fin)

    @classmethod
    def __getattr__(cls, key):
        """Get configuration with key."""
        return cls.config.get(key, {})
