import micropip
whl_url = 'https://g-062a3c.0ed28.75bc.data.globus.org/public/healpy-0.1-py3-none-any.whl'
 micropip.install(whl_url)
await micropip.install("matplotlib")
import healpy
import numpy
