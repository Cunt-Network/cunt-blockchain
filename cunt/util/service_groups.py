from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "cunt_harvester cunt_timelord_launcher cunt_timelord cunt_farmer cunt_full_node cunt_wallet".split(),
    "node": "cunt_full_node".split(),
    "harvester": "cunt_harvester".split(),
    "farmer": "cunt_harvester cunt_farmer cunt_full_node cunt_wallet".split(),
    "farmer-no-wallet": "cunt_harvester cunt_farmer cunt_full_node".split(),
    "farmer-only": "cunt_farmer".split(),
    "timelord": "cunt_timelord_launcher cunt_timelord cunt_full_node".split(),
    "timelord-only": "cunt_timelord".split(),
    "timelord-launcher-only": "cunt_timelord_launcher".split(),
    "wallet": "cunt_wallet cunt_full_node".split(),
    "wallet-only": "cunt_wallet".split(),
    "introducer": "cunt_introducer".split(),
    "simulator": "cunt_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
