# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""
This module contains the classes required for dialogue management.

- DefaultDialogues: The dialogues class keeps track of all dialogues of type default.
- FipaDialogues: The dialogues class keeps track of all dialogues of type fipa.
- LedgerApiDialogues: The dialogues class keeps track of all dialogues of type ledger_api.
- OefSearchDialogues: The dialogues class keeps track of all dialogues of type oef_search.
- SigningDialogues: The dialogues class keeps track of all dialogues of type signing.
"""
from typing import Any

from aea.common import Address
from aea.protocols.base import Message
from aea.protocols.dialogue.base import Dialogue as BaseDialogue
from aea.skills.base import Model

from packages.fetchai.protocols.http.dialogues import HttpDialogue as BaseHttpDialogue
from packages.fetchai.protocols.http.dialogues import HttpDialogues as BaseHttpDialogues
from packages.fetchai.skills.generic_buyer.dialogues import (
    DefaultDialogue as GenericDefaultDialogue,
)
from packages.fetchai.skills.generic_buyer.dialogues import (
    DefaultDialogues as GenericDefaultDialogues,
)
from packages.fetchai.skills.generic_buyer.dialogues import (
    FipaDialogues as GenericFipaDialogues,
)
from packages.fetchai.skills.generic_buyer.dialogues import (
    LedgerApiDialogues as GenericLedgerApiDialogues,
)
from packages.fetchai.skills.generic_buyer.dialogues import (
    OefSearchDialogues as GenericOefSearchDialogues,
)
from packages.fetchai.skills.generic_buyer.dialogues import (
    SigningDialogues as GenericSigningDialogues,
)


DefaultDialogue = GenericDefaultDialogue
DefaultDialogues = GenericDefaultDialogues
FipaDialogues = GenericFipaDialogues
LedgerApiDialogues = GenericLedgerApiDialogues
OefSearchDialogues = GenericOefSearchDialogues
SigningDialogues = GenericSigningDialogues
HttpDialogue = BaseHttpDialogue


class HttpDialogues(Model, BaseHttpDialogues):
    """This class keeps track of all http dialogues."""

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize dialogues.

        :param agent_address: the address of the agent for whom dialogues are maintained
        :return: None
        """
        Model.__init__(self, **kwargs)

        def role_from_first_message(  # pylint: disable=unused-argument
            message: Message, receiver_address: Address
        ) -> BaseDialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return BaseHttpDialogue.Role.CLIENT

        BaseHttpDialogues.__init__(
            self,
            self_address=str(self.skill_id),
            role_from_first_message=role_from_first_message,
        )