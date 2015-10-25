# -*- coding: utf-8 -*-

__all__ = ['SOURCE_PATH', 'OUTPUT_PATH', 'SOURCE_DELIMITER', 'OUTPUT_DELIMITER', 'SOURCE_ENCODING', 'OUTPUT_ENCODING', 'SOURCE_HEADER', 'OUTPUT_HEADER']

SOURCE_PATH = 'data/source/*.txt'
OUTPUT_PATH = 'data/output.csv'
SOURCE_DELIMITER = '|'
OUTPUT_DELIMITER = ','
SOURCE_ENCODING = 'cp949'
OUTPUT_ENCODING = 'utf-8'
SOURCE_HEADER = ['법정동코드', '시도명', '시군구명', '법정음면동명', '법정리명', '산여부', '지번본번', '지번부번', '도로명코드', '도로명', '지하여부', '건물본번', '건물부번', '건축물대장 건물명', '상세건물명', '건물관리번호', '읍면동일련번호', '행정동코드', '행정동명', '우편번호', '우편일련번호', '다량배달처명', '이동사유코드', '고시일자', '변경정도로명주소', '시군구용 건물명', '공동주택여부', '기초구역번호', '상세주소부여여부', '비고1', '비고2']
OUTPUT_HEADER = ['POSTAL CODE', 'OLD ADDRESS', 'NEW ADDRESS(ROAD NAME ADDRESS)']
