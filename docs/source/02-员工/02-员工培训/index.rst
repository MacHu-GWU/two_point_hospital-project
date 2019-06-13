.. _员工培训:

员工培训
==============================================================================

.. contents:: 员工技能
    :depth: 2
    :local:

员工培训介绍
------------------------------------------------------------------------------

**什么是培训**:

游戏中可以建造 ``培训室``, 然后只要给里面配置 ``教师`` 和 ``学员``, 就可以教会你的 ``员工技能`` 了. 注意, 培训无法直接提升员工等级, 员工等级只有在工作中才能提升. 不过有时员工工作经验够了, 需要在最后给予培训才能升级.

**培训教师**:

1. 如果你自己的员工中有人有该项技能, 那么该员工就可以做教师. 培训速度取决于该员工的 ``员工等级`` 和 是否有 ``培训`` 技能 (+50%教学速度 和 学习速度)
2. 如果你自己的员工中没有人有该项技能, 那么可以雇佣一位教师, 价格是一次性雇用价格 $10,000, 每个学员 $5,000. 如果中途取消培训, 培训费不予退回. 外面雇的教师会和病人一样从城外赶来. 雇佣的教师的教学速度较高, 固定 160%.

有些技能只有一个等级, 比如 ``药房管理``, ``注射``. 而有些技能有 5 个等级, 只有学了前一个等级之后, 才能学下一个等级. 比如学习了 ``全科诊断1`` 才能学 ``全科诊断2``.

有些技能本身需要在研究室研究之后, 才能允许进行培训. 比如你需要用具有 ``研究1`` 技能的人研究出 ``研究2`` 技能之后, 才能开始培训 ``研究2``.

**培训所需时间**:

学会一个技能的需求的最小单位是 TU (Training Unit), 中文叫 ``培训点数``. 例如学会 ``全科诊断1`` 需要 240TU. 1TU 相当于 基础培训速度, 也就是 100% 的教师, 在正常游戏速度下, 1 秒钟的培训量. 也就是 4 分钟 可以学会. 大部分的5级技能都是1级需要 240TU, 5级需要 480TU. 另外 240TU 在没有任何技能加成的情况下, 需要培训约 40 天.

**能影响培训速度的因素**:

1. 教师本人的基础教学速度不一定, 可能在 100% ~ 160% 之间不等, 外面雇佣的教师培训速度固定 160%
2. ``培训`` 技能能提高 50% 的教学和学习速度
3. ``老师`` 个性能提高 50% 教学速度
4. ``一学就会`` 个性能提高 50% 学习速度
5. ``笨拙`` 个性能减少 50% 学习速度

**快速培训的技巧**:

- 找具有 ``培训`` 技能, 以及有 ``老师`` 性格的员工进行培训. 不过这样的员工可遇不可求, 不如花钱雇佣外援.
- 购买 ``百科全书书架``, 1 个增加 4% 的培训速度. 如果你建一个超大的房间, 放 25 个书架, 就相当于所有的教师都有 ``培训`` 技能, 以及有 ``老师`` 性格 同时加成的效果了. 也就是培训时间减半.


所有技能一览表
------------------------------------------------------------------------------

.. jinja:: doc_data

    {{ doc_data.lt_staff_skill.render() }}


医生技能
------------------------------------------------------------------------------

.. contents::
    :local:


.. _全科诊断:

全科诊断
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/General-Practice-QIcon.png

- 最高等级: 5
- 加成效果: 每级 +15% 全科诊断技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _精神病学:

精神病学
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Psychiatry-QIcon.png

- 最高等级: 5
- 加成效果: 1 级允许进入精神病室, 2 级开始每级 +20% 精神病诊断和治疗技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _研究:

研究
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Research-QIcon.png

- 最高等级: 5
- 加成效果: 1 级允许进入研究室, 2 级开始每级 +50% 研究技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _手术:

手术
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Surgery-QIcon.png

- 最高等级: 5
- 加成效果: 1 级允许进入手术室, 2 级开始每级 +20% 手术技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _放射科:

放射科
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Radiology-QIcon.png

- 最高等级: 1
- 加成效果: 允许进入超级扫描仪诊断室, 并增加 20% X光诊断技能 (进入X光诊断室无需该技能)
- 培训时间: 240


.. _基因学:

基因学
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Genetics-QIcon.png

- 最高等级: 1
- 加成效果: 允许进入 DNA 实验室
- 培训时间: 240



护士技能
------------------------------------------------------------------------------


.. _药房管理:

药房管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Pharmacy-Management-QIcon.png

- 最高等级: 1
- 加成效果: 药房治疗技能 +20%
- 培训时间: 240


.. _病房管理:

病房管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Ward-Management-QIcon.png

- 最高等级: 5
- 加成效果: 每级 +20% 一般和骨科病房内的诊断和治疗技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _注射管理:

注射管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Injection-Administration-QIcon.png

- 最高等级: 1
- 加成效果: 注射室内的治疗技能 +20%, (进入注射室无需该技能)
- 培训时间: 240


医生和护士通用技能
------------------------------------------------------------------------------


.. _诊断:

诊断
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Diagnostics-QIcon.png

- 最高等级: 5
- 加成效果: 每级 +10% 诊断技能, 适用于所有诊断室
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _治疗:

治疗
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Treatment-QIcon.png

- 最高等级: 5
- 加成效果: 每级 +10% 治疗技能, 适用于所有治疗室
- 培训时间: 240 / 300 / 360 / 420 / 480


助理技能
------------------------------------------------------------------------------


.. _客服:

客服
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Customer-Service-QIcon.png

- 最高等级: 5
- 加成效果: 每级 +50% 客户服务技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _营销:

营销
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Marketing-QIcon.png

- 最高等级: 5
- 加成效果: 1 级允许进入营销室, 2 级开始每级 +20% 营销速度
- 培训时间: 240 / 300 / 360 / 420 / 480


勤杂工技能
------------------------------------------------------------------------------


.. _维修:

维修
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Maintenance-QIcon.png

- 最高等级: 5
- 加成效果: 每级 +30% 机器维修技能
- 培训时间: 240 / 300 / 360 / 360 / 360


.. _机械:

机械
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Mechanics-QIcon.png

- 最高等级: 5
- 加成效果: 1 级允许勤杂工对机器进行升级, 2 级开始每级 +50% 维修技能
- 培训时间: 240 / 300 / 360 / 420 / 480


.. _捉鬼:

捉鬼
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Ghost-Capture-QIcon.png

- 最高等级: 1
- 加成效果: 允许勤杂工侦测鬼魂和抓鬼, 鬼魂由病人死后生成
- 培训时间: 240


员工通用技能
------------------------------------------------------------------------------


.. _临床交流:

临床交流 (只有医生和护士能学)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Bedside-Manner-QIcon.png

- 最高等级: 1
- 加成效果: 跟病人互动时提高病人的幸福度
- 培训时间: 240


.. _情商学:

情商学
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Emotional-Intelligence-QIcon.png

- 最高等级: 1
- 加成效果: 员工自身的幸福度+10%
- 培训时间: 240


.. _体力培训:

体力培训
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Stamina-Training-QIcon.png

- 最高等级: 1
- 加成效果: 体力消耗速度减慢 (减半), 可以和 ``不知疲倦`` 个性的减半叠加, 体力消耗速度变成正常的 25%
- 培训时间: 240


.. _工作激情:

工作激情
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Motivation-QIcon.png

- 最高等级: 1
- 加成效果: 移动速度+10%
- 培训时间: 240


.. _培训达人班:

培训达人班
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./images/Training-Masterclass-QIcon.png

- 最高等级: 1
- 加成效果: 教学和学习速度+50%
- 培训时间: 240



各个房间的员工最佳技能一览表
------------------------------------------------------------------------------

注, 以下所有技能都可以将其中的最后一个换成:

1. 对于全科, 和病房, 可以考虑将其中一个换成

    .. image:: ./images/Stamina-Training-QIcon.png

2. 对于全科, 可以考虑将其中一个换成

    .. image:: ./images/Emotional-Intelligence-QIcon.png

**诊断室**:

- 全科医生办公室:

    .. image:: ./images/General-Practice-QIcon.png
    .. image:: ./images/General-Practice-QIcon.png
    .. image:: ./images/General-Practice-QIcon.png
    .. image:: ./images/General-Practice-QIcon.png
    .. image:: ./images/General-Practice-QIcon.png

- 综合诊断室:

    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png

- 心脏病科:

    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png

- 体液分析:


    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png

- X光室:

    .. image:: ./images/Radiology-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png

- 超级磁力强效共振扫描室:

    .. image:: ./images/Radiology-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png

**治疗室**:

- 药房:

    .. image:: ./images/Pharmacy-Management-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 脱光诊所:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 流行锅实验室:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 小丑诊所:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 色疗室:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 骨科病房:

    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png

- 注射室:

    .. image:: ./images/Injection-Administration-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 有害动物防治:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 手术室:

    .. image:: ./images/Surgery-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 拔头室:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 电疗室:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 分辨率实验室:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 破伊学:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

- 折疗室:

    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

**诊断和治疗**:

- 病房:

    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png
    .. image:: ./images/Ward-Management-QIcon.png

- 精神病室:

    .. image:: ./images/Psychiatry-QIcon.png
    .. image:: ./images/Psychiatry-QIcon.png
    .. image:: ./images/Psychiatry-QIcon.png
    .. image:: ./images/Psychiatry-QIcon.png
    .. image:: ./images/Psychiatry-QIcon.png

- DNA实验室:

    .. image:: ./images/Genetics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Diagnostics-QIcon.png
    .. image:: ./images/Treatment-QIcon.png
    .. image:: ./images/Treatment-QIcon.png

**设施**:

- 接待处:

    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Stamina-Training-QIcon.png

- 员工休息室: 无
- 厕所: 无
- 培训室: 无
- 研究室:

    .. image:: ./images/Research-QIcon.png
    .. image:: ./images/Research-QIcon.png
    .. image:: ./images/Research-QIcon.png
    .. image:: ./images/Research-QIcon.png
    .. image:: ./images/Research-QIcon.png

- 营销室:

    .. image:: ./images/Marketing-QIcon.png
    .. image:: ./images/Marketing-QIcon.png
    .. image:: ./images/Marketing-QIcon.png
    .. image:: ./images/Marketing-QIcon.png
    .. image:: ./images/Marketing-QIcon.png

- 咖啡厅:

    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Customer-Service-QIcon.png
    .. image:: ./images/Stamina-Training-QIcon.png


清洁工:

- 维修清洁工:

    .. image:: ./images/Maintenance-QIcon.png
    .. image:: ./images/Maintenance-QIcon.png
    .. image:: ./images/Maintenance-QIcon.png
    .. image:: ./images/Motivation-QIcon.png
    .. image:: ./images/Stamina-Training-QIcon.png

- 升级清洁工:

    .. image:: ./images/Mechanics-QIcon.png
    .. image:: ./images/Mechanics-QIcon.png
    .. image:: ./images/Mechanics-QIcon.png
    .. image:: ./images/Motivation-QIcon.png
    .. image:: ./images/Stamina-Training-QIcon.png

- 捉鬼清洁工:

    .. image:: ./images/Ghost-Capture-QIcon.png
    .. image:: ./images/Motivation-QIcon.png
    .. image:: ./images/Stamina-Training-QIcon.png
    .. image:: ./images/Emotional-Intelligence-QIcon.png


终极医院需要的员工统计
------------------------------------------------------------------------------

参考资料:

- https://two-point-hospital.fandom.com/wiki/Staff_Training