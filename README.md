southkorea-postal-codes
=======================

This repo hosts South Korea postal codes and related data.

## Description

### Data

* `data/postal_codes_and_addresses.csv`: list of postal codes with addresses **(in submunicipal level)**
* `data/postal_codes_and_latlngs.csv`: list of postal codes with their geographic coordinates **(in submunicipal level)**

### Sources

* `data/postal_codes_and_addresses.csv`: [Korean Data Hub](http://thedatahub.kr/dataset/national-postcode-2012-05)
* Geocoding: [Daum Local API](http://dna.daum.net/apis/local/ref#addr2coord)


## Development Notes

To regenerate `postal_codes_and_latlngs.csv`, follow:

    vi settings.py  # put Daum API key
    python run.py data/postal_codes_and_addresses.csv > data/postal_codes_and_latlngs.csv 2> error.log

**Caution:** Daum API permits only 30,000 API calls per day, per key. You may need to use a couple of keys to get the full list.

## Copyright and License

<a rel="license" href="http://creativecommons.org/licenses/by/2.0/kr/deed.en_US "><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/80x15.png" /></a> ([한국어](http://creativecommons.org/licenses/by/2.0/kr/))
