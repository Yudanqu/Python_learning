一、基本命令
    1、启动服务
        以管理员身份运行cmd
        net start 服务名称
    2、停止服务
        以管理员身份运行cmd
        net stop 服务名称
    3、连接数据库
        格式：mysql - u root - p ->输入密码
    4、退出登录（断开连接）
        exit或quit
    5、查看版本（连接后可以执行）
        select version()
    6、显示当前时间（连接后可以执行）
        select now()
    7、远程连接
        mysql - h ip地址 - u 用户名 - p ->输入对方mysql密码

二、数据库操作命令
    1、创建数据库
        create database 数据库名 charset = utf8
    2、删除数据库
        drop database 数据库名
    3、切换数据库
        use 数据库名
    4、查看当前选择的数据库
        select database()

三、表操作命令
    1、查看数据库中所有表
        show tables
    2、创建表
        create table 表名（列及类型）
        eg：create table student(id int auto_increment primary key,
                                name varchar(20) not null)
        注：auto_increment 自增长   primary key 主键 not null 非空
    3、删除表
        drop table 表名
    4、查看表结构
        desc 表名
    5、查看建表语句
        show create table 表名
    6、重命名表
        rename table 原表名 to 新表名
    7、修改表
        alter table 表名 add | change | drop 列名

四、数据操作命令
    1、增
        a、全列插入
            insert into 表名 values(...)
            eg:
                insert into student values(0, "tom", "北京")
            主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功以后以实际数据为准
        b、缺省插入
            insert into 表名(列1，列2..) values(值1，值2..)
        c、同时插入多条数据
            insert into 表名 values(...), (...), ...
    2、删
        delete from 表名 where 条件
        不写条件则全删
    3、改
        update 表名 set 列1 = 值1, 列2 = 值2, ... where 条件
    4、查
        查询表中的全部数据
        select * from 表名

五、查
    1、基本语法
        select * from 表名
        from关键字后面是表名，表示数据来源于这张表
        select后面写表中的列名，如果是 * 表示在结果集中显示表中额所有列
        在select后面的列名部分，可以使用as为列名起别名，这个别名显示在结果集中
        如果要查询多个列，之间使用逗号分隔
        # eg：select name as a,age from student;
    2、消除重复行
        在select后面列前面使用distinct可以消除重复的行
        eg：select distinct gender from student
    3、条件查询
        a、语法
            select * from 表名 where 条件
        b、比较运算符
            等于（=） 大于（>） 小于（<） 大于等于（>=） 小于等于（<=） 不等于（!= 或 <>）
        c、逻辑运算符
            and or not
        d、模糊查询
            like
            % 表示任意多个任意字符
            _ 表示一个任意字符
        e、范围查询
            in 表示在一个非连续的范围内
            between。。。and。。。 表示在一个连续的范围内
            eg：where id in (8, 10, 13)
        f、空判断
            注意：null与""是不同的
            判断空：is null
            判断非空：is not null
        g、优先级
            小括号，not，比较运算符。逻辑运算符
            and比or优先级高，同时出现并希望先选or，需要结合括号来使用
    4、聚合
        为了快速得到统计数，提供了5个聚合函数
        a、count(*)   表示计算总行数，括号中可以写 * 或列名
        b、max(列)    表示求此列的最大值
        c、min(列)    表示求此列的最小值
        d、sum(列)    表示求此列的和
        e、avg(列)    表示求此列的平均值
    5、分组
        按照字段分组，表示此字段相同的数据会被放到一个集合中。分组后，只能查询出相同的数据列，对于有差异的数据列无法显示在结果集中
        可以对分组后的数据进行统计，做聚合运算
        select 列1, 列2, 聚合... from 表名 group by 列1, 列2 having 列1, 列2
        eg:
            查询男女生总数
            select gender, count(*) from student group by gender
        where与having的区别：where是对from后面指定的表进行筛选，属于对原始数据的筛选；having是对group by的结果进行筛选。
    6、排序
        select * from 表名 order by 列1 asc | desc, 列2 asc | desc, ...
        a、将数据按照列1进行排序，如果某些列1的值相同则按照列2排序
        b、默认按照从小到大的顺序
        c、asc升序
        d、desc降序
    7、分页
        select * from 表名 limit start, count
        从start开始，看count条

六、关联
    建表语句
    1、create table class(id int auto_increment primary key, name varchar(20) not null, stuNum int not null)
    2、create table students(id int auto_increment primary key, name varchar(20) not null, gender bit default 1, classid int not bull, foreign key(classid) references class(id))

    插入一些数据：
    insert into class values(0, "python1", 50), (0, "python2", 60), (0, "python3", 70)

    insert into students values(0, "tom", 1, 1)

    关联查询：
    select students.name, class.name from class inner join students on class.id = students.classid

    分类：
        1、表A inner join 表B
            表A与表B匹配的行会出现在结果集中
        2、表A left join 表B
            表A与表B匹配的行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充
        3、表A right join 表B
            表A与表B匹配的行会出现在结果集中，外加表B中独有的数据，未对应的数据使用null填充
