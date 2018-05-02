import re

def analysis_response(correlation, response):
        correlationDict = {}
        '''
        用于解析返回值中的数据，将这些数据存入关联字典中以供使用
        :param response : 接口返回值
        :return:
        '''
        # 如果关联数据不为空
        if correlation != '':
            # 1.处理关联数据(存到列表中)
            correlation = correlation.replace('\n', '').replace('\r',
                                                                '').split(';')

            print('correlation = ',correlation)

            # 2.分解关联数据
            for j in range(len(correlation)):
                print('correlation的长度为：',len(correlation))
                print('j = ',j)

                param = correlation[j].split('=')
                print('处理后的correlation = ',correlation)

                
                # 3.判断处理后的关联列表长度为2时
                if len(param) == 2:
                    if param[1] == '' or not re.search(
                            r'^\[', param[1]) or not re.search(
                                r'\]$', param[1]):
                        continue

                    # 4.返回结果赋值
                    value = response

                    # 5.继续处理correlation
                    a = param[1][1:-1].split('][')

                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                        except:
                            try:
                                temp = value[key]
                            except:
                                break
                        value = temp
                        print('value = ',value)
                    correlationDict[param[0]] = value
        return correlationDict


correlation = "${team_id}=[team_id];${space_id}=[space][space_id]"

response = {
    'team_id':1,
    'space':{
        'space_id':2
    }
}
a = analysis_response(correlation,response)
print('a = ',a)




