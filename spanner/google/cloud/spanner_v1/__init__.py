# Copyright 2017, Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import pkg_resources
__version__ = pkg_resources.get_distribution('google-cloud-spanner').version

from google.cloud.spanner_v1 import param_types
from google.cloud.spanner_v1 import types
from google.cloud.spanner_v1.client import Client
from google.cloud.spanner_v1.gapic import enums
from google.cloud.spanner_v1.keyset import KeyRange
from google.cloud.spanner_v1.keyset import KeySet
from google.cloud.spanner_v1.pool import AbstractSessionPool
from google.cloud.spanner_v1.pool import BurstyPool
from google.cloud.spanner_v1.pool import FixedSizePool


COMMIT_TIMESTAMP = 'spanner.commit_timestamp()'
"""Placeholder be used to store commit timestamp of a transaction in a column.

This value can only be used for timestamp columns that have set the option 
``(allow_commit_timestamp=true)`` in the schema.
"""


__all__ = (
    # google.cloud.spanner_v1
    '__version__',
    'param_types',
    'types',

    # google.cloud.spanner_v1.client
    'Client',

    # google.cloud.spanner_v1.keyset
    'KeyRange',
    'KeySet',

    # google.cloud.spanner_v1.pool
    'AbstractSessionPool',
    'BurstyPool',
    'FixedSizePool',

    # google.cloud.spanner_v1.gapic
    'enums',

    # local
    'COMMIT_TIMESTAMP',
)
