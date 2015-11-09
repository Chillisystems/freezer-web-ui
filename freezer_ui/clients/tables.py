# (c) Copyright 2014,2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging

from django.utils.translation import ugettext_lazy as _
from horizon import tables


LOG = logging.getLogger(__name__)


class ClientsTable(tables.DataTable):
    client_id = tables.Column('client_id', verbose_name=_("Client ID"))
    name = tables.Column('hostname', verbose_name=_("Hostname"))

    class Meta:
        name = "clients"
        verbose_name = _("Clients")
        row_actions = ()
        table_actions = ()
        multi_select = False
