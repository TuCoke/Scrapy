# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from timework.sqlhelper import DBHelper


class TimeworkPipeline:
    def process_item(self, item, spider):
        _mysql = DBHelper()
        print(f"item", item)
        sql = "SELECT copy_id,company_name FROM workTime  WHERE copy_id =%s"
        arg = (item['Id'])
        print(f"item的id值", item['Id'])
        result = _mysql.exit_id(sql, arg)
        if result is None:
            _work_sql = 'INSERT INTO `workTime`' \
                        '(company_name,department_name,base,start_time,end_time,create_time,copy_id) ' \
                        'VALUES(%s,%s,%s,%s,%s,%s,%s)'
            _work_arg = (item['company_name'], item['department_name'], item['base'], item['start_time'],
                         item['end_time'], item['create_time'], item['Id'])
            result_insert = _mysql.insert(_work_sql, _work_arg)
            print(f"返回", result)
            print(f'插入返回', result_insert)

            _detail_sql = "INSERT INTO `detailWork`" \
                          "(source,open_id,industry_name,job_category,occupation,lunch_time,dinner_time," \
                          "working_days,remark,work_id) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            _detail_arg = (item['source'], str(item['open_id']), item['industry_name'], item['job_category'],
                           item['occupation'], item['lunch_time'], item['dinner_time'], item['working_days']
                           , item['remark'], item['Id']
                           )
            result_detail_id = _mysql.insert(_detail_sql, _detail_arg)
            print(f"详情插入的id", result_detail_id)

        else:
            print(f"已经存在这条数据", item['Id'])
        return item
