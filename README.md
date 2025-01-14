# Volvo Cars Home Assistant integration

This integration provides access to your Volvo car, provided your model and region are supported by their API. Supported regions include: Europe, Middle East, and Africa. For a full list of supported countries, visit [Volvo's API documentation](https://developer.volvocars.com/terms-and-conditions/apis-supported-locations/).

Now check out the features section for details on what you'll get!

[![GitHub release (with filter)][releases-shield]][releases]

## ✨ Features

### General

- Multiple cars
- Multiple accounts
- Translations (but [need help](#contributing) on this 🙏)

### Entities

This integration will give you about 70 entities! Some may only be added if it is supported by your car.

#### Binary sensors

- Diagnostics: car availability, service, washer fluid, brake fluid
- Doors open/closed: front, back, hood, tailgate, tank lid
- Engine status: running, coolant level, oil level
- Light warnings: brakes, daytime lights, fog lights, hazard lights, high & low beam lights, position lights, registration plate, reverse light, side mark lights, turn indicators
- Tyre pressure warnings
- Windows open/closed: front, back, sunroof

Some sensors provide extra information in the attributes, like reason, pressure or level.

#### Buttons

- Start/stop climatization
- Start/stop engine
- Flash
- Honk
- Honk & flash

The action's status is included in the attributes.

#### Tracking

- Location tracking, including heading direction

#### Images

- Multiple exterior images from different angles
- Interior

#### Locks

- Lock
- Lock with reduced guard
- Unlock

The action's status is included in the attributes.

#### Sensors

- Volvo API status
- Energy and/or fuel consumption
- Average speed
- Fuel amount
- Battery capacity
- Battery charge level
- Charging connection
- Charging status
- Estimated charging time
- Distance to empty battery / tank
- Distance to service
- Engine hours to service
- Time to service
- Odometer
- Trip meter

## 🛠️ Installation

### Requirements

- [Home Assistant](https://www.home-assistant.io/) v2024.11.0 or later.

- [Home Assistant Community Store (HACS)](https://hacs.xyz/).

- You'll also need a Volvo developer account to use this integration. Don't worry, it's free of charge!

  1. Head over to https://developer.volvocars.com/ and make an account.
  2. Once signed in, go to https://developer.volvocars.com/account/#your-api-applications and create an "API application". Give it some meaningful name.
  3. Repeat step 2 for every additional car **on this account** that you'd like to use with this integration. Repeat the whole process if you have cars on different accounts.

### Install

Add this repository to your HACS with the following button:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=thomasddn&repository=ha-volvo-cars&category=integration)

Install this integration with the follwing button:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=volvo_cars)

### Adding your car

Adding your car involves two steps. You'll need to repeat this process for each car you want to add, even if they are on the same account.

Remember to generate an API key for every car. There is a limit on the number of API requests per key.

#### Step 1: fill in credentials

| Field                         | Description                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| Username                      | The username of your Volvo developer account.                                                         |
| Password                      | The password of your Volvo developer account.                                                         |
| Vehicle Identification Number | The VIN of the car you want to add.                                                                   |
| Volvo API key                 | The generated API key in the developer account.                                                       |
| Friendly name                 | This value is used in the entity ID (volvo\_[friendly name]\_[key]). If left empty, VIN will be used. |

After submitting, a One Time Password (OTP) will be sent to your email. It's a 6 digit number.

#### Step 2: OTP

Fill in the OTP to complete the process.

<a name="contributing"></a>

### Options

Once a car has been added, you can configure additional options for it.

| Option                  | Description                                                  | Availability                                          |
| ----------------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Fuel consumption unit   | You can choose between `l/100km`, `mpg (UK)` and `mpg (US)`. | Cars with a combustion engine.                        |
| Images background color | Choose the background color for the exterior images.         | Depending on the image URL provided by the Volvo API. |

## 🤝 Contributing

You can contribute by creating a PR, but also by testing:

- Provide general feedback or report issues.
- Help with translations.
- Test if you have multiple Volvos on the **same account**.
- ~~Test if you have multiple Volvos across **different accounts**.~~
- ~~Test with other Volvo models (non-BEV).~~
- ~~Users that use imperial system.~~

Shoutout to [@Pau1ey](https://github.com/Pau1ey) for testing and confirming this! 🤩

## 🛟 Need help?

If you have a feature request or encounter a problem, feel free to open an issue! Have a general question, need help setting up, or want to show off your Volvo dashboard? Go to the discussions.

You can also join the [thread on the HA community](https://community.home-assistant.io/t/volvo-cars-integration/796417/).

## 🥤 Powered by snacks

When I'm coding, I run on coffee, Coca-Cola*, and Lays* potato chips. If you'd like to show your appreciation for this project, consider making a small donation to help keep my stash stocked! (Note: I’m also happy to accept 1,000,000 USD — or EUR, I’m not picky. 😁)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N7UZ6KN)

<sub><sub>\* No affiliation with these brands — just personal favorites!</sub></sub>

[releases-shield]: https://img.shields.io/github/v/release/thomasddn/ha-volvo-cars?style=flat-square
[releases]: https://github.com/thomasddn/ha-volvo-cars/releases
