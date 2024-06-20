# _*_ coding:utf-8 _*_
"""
作者: LiXX
日期: 2024年06月16日
"""
import requests
import pytest


BAIDU_URL = "http://www.baidu.com/s"

# 字数限制
def test_input_limit():
    input = "a" * 100
    response = requests.get(BAIDU_URL, params={'wd': input})
    assert len(response.url.split('wd=')[1]) <= 100, "超过限制字符了"


# 测任意语言
@pytest.mark.parametrize("input_language", [
    "测试中文",
    "test english"
])
def test_input_language(input_language):
    input = input_language
    response = requests.get(BAIDU_URL, params={'wd': input})
    assert response.status_code == 200


# 实际只要前20个字符
@pytest.mark.parametrize("query", [
    "a",  # 单个字符
    "a" * 20,  # 正好20个字符
    "a" * 50,  # 超过20个字符
])
def test_real_input(query):
    response = requests.get(BAIDU_URL, params={'wd': query})
    #assert response.url.split('wd=')[1] == query[:20]
    res_query = response.url.split('wd=')[1]
    assert len(res_query) <= 20, "搜索超过20个字符"
    if len(res_query) > 20:
        assert res_query == query[:20], "未截取到前20个字符"

# 为空
def test_empty():
    response = requests.get(BAIDU_URL)
    #assert "www.baidu.com" in response.url
    assert "http://www.baidu.com/s" in response.url


# 无结果  按实际返回写“”内容
def test_no_result():
    input = "百度搜索功能接口文档https://doc.poc.ceshiren.com/"
    response = requests.get(BAIDU_URL, params={'wd': input})
    assert "抱歉，未找到相关结果。" in response.text

# 有结果
def test_has_result():
    input = "测试"
    response = requests.get(BAIDU_URL, params={'wd': input})
    assert "百度为您找到以下结果" in response.text

# 忽略<>
def test_special_characters():
    response = requests.get(BAIDU_URL, params={'wd': '就是有<和>'})
    assert '<' not in response.url and '>' not in response.url


