#!/usr/bin/env python

#
# GRAKN.AI - THE KNOWLEDGE GRAPH
# Copyright (C) 2018 Grakn Labs Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from __future__ import print_function
import tarfile
import json

import sys


def tarfile_remove_mtime(info):
    info.mtime = 0
    return info


_, moves_file_location, distribution_tgz_location, version_file_location = sys.argv
with open(moves_file_location) as moves_file:
    moves = json.load(moves_file)

with open(version_file_location) as version_file:
    version = version_file.read().strip()

with tarfile.open(distribution_tgz_location, 'w:gz', dereference=True) as tgz:
    for fn, arcfn in sorted(moves.items()):
        tgz.add(fn, arcfn.replace('{pom_version}', version), filter=tarfile_remove_mtime)
