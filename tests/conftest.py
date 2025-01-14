"""Test fixtures for Volvo Cars."""

from unittest.mock import AsyncMock, MagicMock, patch

from _pytest.fixtures import SubRequest
import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.volvo_cars.const import CONF_VCC_API_KEY, CONF_VIN, DOMAIN
from custom_components.volvo_cars.coordinator import VolvoCarsData
from custom_components.volvo_cars.store import StoreData, create_store
from custom_components.volvo_cars.volvo.auth import VolvoCarsAuthApi
from custom_components.volvo_cars.volvo.models import (
    AuthorizationModel,
    TokenResponse,
    VolvoCarsAvailableCommand,
    VolvoCarsLocation,
    VolvoCarsValue,
    VolvoCarsValueField,
    VolvoCarsVehicle,
)
from homeassistant.const import CONF_FRIENDLY_NAME, CONF_USERNAME
from homeassistant.core import HomeAssistant

from .common import load_json_object_fixture


@pytest.fixture
async def mock_config_entry(hass: HomeAssistant) -> MockConfigEntry:
    """Return the default mocked config entry."""
    config_entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id="YV1ABCDEFG1234567",
        data={
            CONF_USERNAME: "john@doe.com",
            CONF_VIN: "YV1ABCDEFG1234567",
            CONF_VCC_API_KEY: "abcdefghij0123456789",
            CONF_FRIENDLY_NAME: "myvolvo",
        },
    )

    store = create_store(hass, config_entry.unique_id)
    await store.async_save(StoreData(access_token="", refresh_token=""))

    config_entry.runtime_data = VolvoCarsData(MagicMock(), store)
    config_entry.add_to_hass(hass)

    return config_entry


@pytest.fixture(autouse=True)
async def mock_api(request: SubRequest):
    """Mock APIs."""

    marker = request.node.get_closest_marker("use_model")
    model = marker.args[0] if marker is not None else "xc40_bev"

    with (
        patch.object(VolvoCarsAuthApi, "async_refresh_token") as mock_auth_api,
        patch(
            "custom_components.volvo_cars.VolvoCarsApi",
            autospec=True,
        ) as mock_api,
    ):
        vehicle_data = load_json_object_fixture(f"vehicle_{model}.json")
        vehicle = VolvoCarsVehicle.from_dict(vehicle_data)

        commands_data = load_json_object_fixture("commands.json").get("data")
        commands = [VolvoCarsAvailableCommand.from_dict(item) for item in commands_data]

        location_data = load_json_object_fixture("location.json")
        location = {"location": VolvoCarsLocation.from_dict(location_data)}

        availability = _get_json_as_value_field("availability.json")
        brakes = _get_json_as_value_field("brakes.json")
        diagnostics = _get_json_as_value_field("diagnostics.json")
        doors = _get_json_as_value_field("doors.json")
        engine_status = _get_json_as_value_field("engine_status.json")
        engine_warnings = _get_json_as_value_field("engine_warnings.json")
        fuel_status = _get_json_as_value_field("fuel_status.json")
        odometer = _get_json_as_value_field("odometer.json")
        recharge_status = _get_json_as_value_field("recharge_status.json")
        statistics = _get_json_as_value_field("statistics.json")
        tyres = _get_json_as_value_field("tyres.json")
        warnings = _get_json_as_value_field("warnings.json")
        windows = _get_json_as_value_field("windows.json")

        api = mock_api.return_value
        api.async_get_api_status = AsyncMock(
            return_value={"apiStatus": VolvoCarsValue("OK")}
        )
        api.async_get_availability_status = AsyncMock(return_value=availability)
        api.async_get_brakes_status = AsyncMock(return_value=brakes)
        api.async_get_commands = AsyncMock(return_value=commands)
        api.async_get_diagnostics = AsyncMock(return_value=diagnostics)
        api.async_get_doors_status = AsyncMock(return_value=doors)
        api.async_get_engine_status = AsyncMock(return_value=engine_status)
        api.async_get_engine_warnings = AsyncMock(return_value=engine_warnings)
        api.async_get_fuel_status = AsyncMock(return_value=fuel_status)
        api.async_get_location = AsyncMock(return_value=location)
        api.async_get_odometer = AsyncMock(return_value=odometer)
        api.async_get_recharge_status = AsyncMock(return_value=recharge_status)
        api.async_get_statistics = AsyncMock(return_value=statistics)
        api.async_get_tyre_states = AsyncMock(return_value=tyres)
        api.async_get_vehicle_details = AsyncMock(return_value=vehicle)
        api.async_get_warnings = AsyncMock(return_value=warnings)
        api.async_get_window_states = AsyncMock(return_value=windows)

        mock_auth_api.return_value = AuthorizationModel(
            "COMPLETED",
            token=TokenResponse(
                access_token="",
                refresh_token="",
                token_type="Bearer",
                expires_in=1799,
                id_token="",
            ),
        )

        yield


def _get_json_as_value_field(filename: str) -> dict:
    data = load_json_object_fixture(filename)
    return {key: VolvoCarsValueField.from_dict(value) for key, value in data.items()}
