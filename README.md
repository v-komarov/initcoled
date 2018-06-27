## Инструменты первоначальной загрузки в topics из dim.employee и dim.person ##

- **initcoled.py** (job загрузки в топики person и employee из PostgreSQL dim.employee и dim.person Загружаемые данные: id записи и face descriptor)
- **load_topic_test.py** (job тестовой загрузки в топики - можно выбратьв какой)
- **conf.py** (реквизиты для подключения к PostgreSQL и kafka)
- **test_data.json** (Набор тестовых данных в формате json)
- **kafka.service** **zookeeper.service** (для systemd . Каталог размещения /etc/systemd/system/)