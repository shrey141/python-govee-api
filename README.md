# govee_api

Python client for the [Govee API](https://developer.govee.com) to control LED strips and bulbs from Home Assistant or any Python project.

> **Note:** This library powers the [shrey141/hacs-govee](https://github.com/shrey141/hacs-govee) Home Assistant integration.

## Installation

```bash
pip install git+https://github.com/shrey141/python-govee-api.git
```

## Usage

See the [`/example`](example/) folder for complete working examples. Basic usage:

```python
import asyncio
from govee_api import Govee, GoveeNoLearningStorage

async def main():
    async with Govee("YOUR_API_KEY", learning_storage=GoveeNoLearningStorage()) as client:
        devices, err = await client.get_devices()
        if err:
            print(f"Error: {err}")
            return
        for device in devices:
            print(f"{device.device_name} ({device.model})")
            await client.turn_on(device)

asyncio.run(main())
```

## API Key

Open the **Govee Home** app → Account → Settings → **About Us** → **Apply for API Key**. The key is emailed to your account address within minutes.

## Rate Limits

The Govee API allows **10,000 requests per account per day**. Each `get_states()` call makes one request per device. Plan your poll interval accordingly.

## Features

- Turn devices on/off
- Set brightness (0–254)
- Set color (RGB)
- Set color temperature (2000–9000 K)
- Poll device state
- Learned device settings persisted via pluggable storage
- Online/offline event callbacks
- Assumed state after commands (reduces perceived lag)

## Govee Trademark

Govee and the Govee logo are trademarks or registered trademarks of Shenzhen Intellirock Company Limited. Use of the Govee name refers to the third-party API service this library communicates with.

## Development

```bash
pip install setuptools wheel tox
# clone, make a feature/NAME or bug/NAME branch
tox  # run tests
```

## Issues

Report bugs at [github.com/shrey141/python-govee-api/issues](https://github.com/shrey141/python-govee-api/issues)

## License

MIT — see [LICENSE](LICENSE)
