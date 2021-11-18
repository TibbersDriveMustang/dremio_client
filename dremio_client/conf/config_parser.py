# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Ryan Murray.
#
# This file is part of Dremio Client
# (see https://github.com/rymurr/dremio_client).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import os
import shutil
import logging

import confuse

DEBUG = False

def _get_env_args():
    args = dict()
    #TODO DREMIO_CLIENTDIR not in use
    for k, v in os.environ.items():
        if "DREMIO_" in k and k != "DREMIO_CLIENTDIR":
            name = k.replace("DREMIO_", "").lower().replace("_", ".")
            if name == "port" or name == "auth.timeout":
                v = int(v)
            elif name == "ssl":
                v = v.lower() in ["true", "1", "t", "y", "yes", "yeah", "yup", "certainly", "uh-huh"]
            args[name] = v
    return args

def build_config(args=None):
    config = confuse.Configuration("dremio_client", __name__)
    config['isAE'] = False
    if 'ANACONDA_PROJECT_ENVS_PATH' in os.environ or DEBUG:
        logging.warning('AE env detected')
        if DEBUG:
            AE_DEFAULT_SECRET_PATH = '/Users/hongyiguo/Desktop/HKEX/Sanctum/dremio_client/dremio_client/dremio_client'
            DREMIO_CONFIG_PATH = '/Users/hongyiguo/Desktop/HKEX/Sanctum/dremio_client/tests/config.yaml'
        else:
            AE_DEFAULT_SECRET_PATH = '/var/run/secrets/user_credentials/dremio_client'
            DREMIO_CONFIG_PATH = '/opt/continuum/.config/dremio_client/config.yaml'

        # if 'DREMIO_CLIENTDIR' in os.environ:
        #     config.set_file(os.environ["DREMIO_CLIENTDIR"] + '/dremio_client')
        if os.path.isfile(AE_DEFAULT_SECRET_PATH):
            # Check AE Secret path
            shutil.copy(AE_DEFAULT_SECRET_PATH, DREMIO_CONFIG_PATH)
            config.set_file(DREMIO_CONFIG_PATH)
            config['isAE'] = True
        else:
            raise NotImplementedError("Found no Dremio credential, please config your AE Secret")

    if args:
        config.set_args(args, dots=True)
    env_args = _get_env_args()
    config.set_args(env_args, dots=True)
    config["auth"]["password"].redact = True
    return config
