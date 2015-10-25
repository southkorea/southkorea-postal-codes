대한민국 우편번호/southkorea-postal-codes
=======================

이 레포지토리는 대한민국 구주소(지번주소), 신주소(도로명주소), 신우편번호(다섯자리) 데이터를 제공합니다.
This repo hosts South Korea postal codes and address(including road name address).

## 설명/Description

### 데이터/Data

* [data/output.csv]()
  * 신우편번호(다섯자리), 구주소(지번주소), 신주소(도로명주소) 목록
  * list of postal codes with addresses(including road name address) **(in submunicipal level)**
  * `output.csv` 파일은 제 [드랍박스](https://www.dropbox.com/s/92xxezm770a74g4/output.csv?dl=0)를 통해서 다운로드 받으실 수 있습니다.
  * You can download `output.csv` file from [my dropbox](https://www.dropbox.com/s/92xxezm770a74g4/output.csv?dl=0).

### 데이터 출처/Sources

* [juso.go.kr](http://www.juso.go.kr/support/AddressBuild.do)
* (원본 파일 크기가 너무 커서 깃헙에 업로드가 불가능합니다. 원본 데이터는 제 [드랍박스](https://www.dropbox.com/s/c8cceqg1ebxbkbi/source.zip?dl=0)를 통해서 다운로드 받으실 수 있습니다.)
* (the size of original data is not enough to upload on gihtub, so that you can download the original data(txt files) from [my dropbox](https://www.dropbox.com/s/c8cceqg1ebxbkbi/source.zip?dl=0))


## Development Notes

`data/output.csv` 생성하려면 다음을 실행하세요
To regenerate `data/output.csv`, follow:

```bash
    unzip source.zip -d /path/to/repo/data/ #zip file you downloaded from my dropbox
    python run.py
```

## 저작권/Copyright and License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/kr/deed.en_US "><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/80x15.png" /></a> ([한국어](http://creativecommons.org/licenses/by/4.0/kr/))
