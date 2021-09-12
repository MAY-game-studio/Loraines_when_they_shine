
image bg5_1:
    contains:
        "images/背景/夜空.jpg"
        size(1920,1080)

image bg5_2:
    contains:
        "images/背景/魔法店内景.png"
        size(1920,1080)

image cg5_1:
    contains:
        "images/cg/睡着的琴伊A.png"
        size(1920,1080)

image cg5_2:
    contains:
        "images/cg/睡着的琴伊B.png"
        size(1920,1080)

screen Side_noki_1:
    zorder 100
    add "noki 1" xpos -170 ypos 700

label chapter_4:
    scene bg5_1

    narrator "转眼间，夜幕已经降临。"

    scene bg5_2
    with dissolve

    show noki 4:
        xpos 607
        ypos 80
    with dissolve

    N "然后是糖和蜂蜜……蜂蜜，蜂蜜放在哪儿了……?"

    show noki 12:
        xpos 607
        ypos 80
    with dissolve

    N "让我找找看……啊，蜂蜜在这里。"

    show noki 18:
        xpos 607
        ypos 80
    with dissolve

    N "怎么只剩这么点了!"

    show noki 20:
        xpos 607
        ypos 80
    with dissolve

    N "真是的……琴伊姐也不愿意告诉我配方，只能慢慢尝试了。"

    "我用勺子舀了一小勺蜂蜜，放进了用干洛兰花瓣泡出来的茶水中。"

    show noki 8:
        xpos 607
        ypos 80
    with dissolve

    "搅拌，搅拌……"

    "等勺子上的蜂蜜完全溶解之后，我轻轻舀起了一勺蜂蜜花茶。"

    "因为没有任何经验可以参考，现在只能一边调配一边品尝了。"

    show noki 11:
        xpos 607
        ypos 80
    with dissolve

    N "呜!好烫!"

    "茶水是刚刚泡出来的，依然冒着热气。"

    show noki 14:
        xpos 607
        ypos 80
    with dissolve

    N "嗯……还是不够甜。"

    show noki 9:
        xpos 607
        ypos 80
    with dissolve

    N "再加一勺糖吧。"

    show noki 19:
        xpos 607
        ypos 80
    with dissolve

    N "嗯……不只是不够甜，花的味道不太明显，是不是应该泡得更浓一些?"

    "我瞟了一眼装干花瓣的袋子，还剩下很多花瓣，肯定是够用了。"

    show noki 8:
        xpos 607
        ypos 80
    with dissolve

    N "那就再泡一壶吧~"

    scene bg5_2
    with fade
    ## 原地转场

    show noki 1:
        xpos 607
        ypos 80
    with dissolve

    N "嗯~ "

    show noki 10:
        xpos 607
        ypos 80
    with dissolve

    N "这次还差不多。"

    "在不断的调味和品尝之后，现在我面前摆着一杯精心制成的蜂蜜洛兰花特饮。"

    "无论是蜂蜜的甜味，还是花瓣的清香，都已经搭配到了堪称完美。"

    show noki 12:
        xpos 607
        ypos 80
    with dissolve

    "温度也是刚刚好的程度：并不烫嘴，但余温还未散去，依然可以坚持一段时间不变凉。"

    "对于没有任何经验的第一次尝试来说，估计这已经是我所能达到的最高水平了。"

    "说是凝结了我终极的料理技巧与心意的成品也不为过。"

    show noki 2:
        xpos 607
        ypos 80
    with dissolve
    "琴伊姐尝到的时候，会是什么表情呢?"

    "还真是期待啊……"

    "我小心翼翼地端起杯子，走向了琴伊姐的房间。"

    scene black
    with dissolve
    scene bg5_2
    with dissolve

    show noki 8:
        xpos 607
        ypos 80
    with dissolve

    "（敲门）"

    show noki 4:
        xpos 607
        ypos 80
    with dissolve

    N "琴伊姐?在嘛——"

    "……"

    "没有回应。"

    show noki 7:
        xpos 607
        ypos 80
    with dissolve

    "不对啊，这个时候应该是琴伊姐研究的中间休息时间。"

    "就算琴伊姐正在忙，也不会没有反应吧?"

    show noki 12:
        xpos 607
        ypos 80
    with dissolve

    "嗯……说不定是读书太专注了，我还是大点声吧。"

    show noki 9:
        xpos 607
        ypos 80
    with dissolve
    N "琴——伊——姐——!"

    N "在——吗——?"

    "……"

    "依然没有回应。"

    show noki 18:
        xpos 607
        ypos 80
    with dissolve

    N "嘛……算了，可能是琴伊姐有什么事情，现在恰好不在屋里。"

    show noki 12:
        xpos 607
        ypos 80
    with dissolve

    N "我等一会儿再来吧。"

    show noki 8:
        xpos 607
        ypos 80
    with dissolve

    N "正好可以把花茶再热一下，现在已经有点凉了。"

## nvl模式

    scene bg5_2

    "一刻钟后。*再行讨论演出效果"


    show noki 9:
        xpos 607
        ypos 80
    with dissolve

    N "（敲门）*?"

    N "琴伊姐?"

    "……"

    show noki 19:
        xpos 607
        ypos 80
    with dissolve

    "奇怪了，怎么还是没有回应"

    "难道琴伊姐出门了?不对啊，今天晚上应该没有什么事情。"

    show noki 18:
        xpos 607
        ypos 80
    with dissolve

    "而且琴伊姐如果要出门，肯定会告诉我的。"

    "难道是……下午惹她生气了?"

    show noki 14:
        xpos 607
        ypos 80
    with dissolve

    "我应该没做什么惹她生气的事情吧……"

    show noki 7:
        xpos 607
        ypos 80
    with dissolve
    "难道是买的糖果太多了?但是最后不是去掉了一大半吗?"

    show noki 14:
        xpos 607
        ypos 80
    with dissolve
    "还是说……买花的事情惹她生气了?"

    "虽然我不知道是怎么回事，但是按照当时那个情况，琴伊姐绝对是认识洛兰花的。"

    show noki 6:
        xpos 607
        ypos 80
    with dissolve
    "难道是因为这个在生我的闷气吗……"

    show noki 19:
        xpos 607
        ypos 80
    with dissolve
    "但是我看她后来的样子，也完全不像是生气了。"

    "倒不如说……不管怎么说，琴伊姐都不可能完全不理我吧。"

    "等等……"

    show noki 11:
        xpos 607
        ypos 80
    with dissolve
    "不会是做研究的时候，遇到了什么意外吧?!"

    N "千万别……!"

    "就在这个可能性跳进脑海的一瞬间，我已经推开了房门。"

## 直接跳转，推开门的效果
## CG：睡着的琴伊-闭眼（以下表示小头像表情，没有标识表示没有小头像而非小头像不变）
    scene white
    scene cg5_1
    with dissolve

    N "琴伊jie……*我自己改了一下演出"
    show noki 11 onlayer overlay:
        xpos -170
        ypos 700
    "看到房间里的状况后，我赶紧降低了声音。"
    show noki 11 onlayer overlay:
        xpos -170
        ypos 700
    "琴伊姐，睡着了?"
    show noki 11 onlayer overlay:
        xpos -170
        ypos 700
    "原来是这样，难怪一直没有回应我。"
    show noki 11 onlayer overlay:
        xpos -170
        ypos 700
    "我小心地走进屋，把端在手里的热饮放在了她面前的书桌上。"
    show noki 11 onlayer overlay:
        xpos -170
        ypos 700
    "她依然一动不动地趴在桌子上，看来我的出现并没有吵醒她。"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    N "琴伊……姐?"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "琴伊姐的手里还握着笔，面前的桌子上也堆放着书籍和一些草稿，似乎都是关于魔法研究的。"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "看来……琴伊姐大概是在看书的时候不小心睡着了啊。"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "我看书的时候倒是经常睡着，不过想不到一向对魔法非常认真的琴伊姐也会这样啊。"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "可能是下午和我一起逛街太累了吧。"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "诺琪" "{size=20}\"琴……伊……姐……\""
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "我小声呼唤了她几声，但好像没能唤醒她。"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "现在应该做什么……要叫醒她吗?"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "还是不要打扰琴伊姐比较好?"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "但是如果我就这样走掉了，等她醒来的时候，泡好的洛兰花茶大概就已经凉了吧?"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "有些不知所措的我，下意识看向了桌子上散落的纸张。"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "上面的字都是手写的，大概是琴伊姐的研究笔记什么的。"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "琴伊姐在研究什么呢……?"
    show noki 4 onlayer overlay:
        xpos -170
        ypos 700
    "不知道和我正在学的东西有没有关联。"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "诺琪" "{size=20}\"琴伊姐，我就好奇一下下……\""
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "我轻轻拨开了散落在桌面上的长发。"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "然后从一堆手稿里，抽出了最上面的一张。"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "可能是因为发出的声音很小，琴伊姐并没有醒来的迹象。"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "我试图阅读纸上的内容。"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "…"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "……"
    show noki 9 onlayer overlay:
        xpos -170
        ypos 700
    "………"
    show noki 5 onlayer overlay:
        xpos -170
        ypos 700
    "诺琪" "{size=20}\"这真的是魔法吗……\""
    show noki 5 onlayer overlay:
        xpos -170
        ypos 700
    "我试图集中精神，再看一遍。"
    show noki 6 onlayer overlay:
        xpos -170
        ypos 700
    "……"
    show noki 6 onlayer overlay:
        xpos -170
        ypos 700
    "结果得到了和刚才相同的结果。"
    show noki 6 onlayer overlay:
        xpos -170
        ypos 700
    "完 全 没 看 懂 !*演出效果待定"
    show noki 6 onlayer overlay:
        xpos -170
        ypos 700
    "手稿上写满了没有注释的箭头、图示和数字。"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "箭头……从一个人到另一个人，是代表魔法标记的移动?或者是魔力的移动?"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    N "也许是白天我瞎想的那个转移魔力的方法?"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "我对于魔法并非一窍不通，不如说已经用了许多年了，也算是熟悉。"
    show noki 7 onlayer overlay:
        xpos -170
        ypos 700
    "然而看到这些笔记，我唯一能看出来的，也就是它和魔法有一些联系了。"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    N "算了……这些东西对我来说也太难了。"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    "我默默把手稿放回了原来的位置。"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    "琴伊姐依然没有要醒过来的迹象，原来她睡觉这么沉吗，我之前都不知道……"

## CG放大，聚焦到琴伊

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "诺琪" "{size=20}\"琴伊姐……\""

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "如果现在睡太久，晚上会睡不着觉吧。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "所以，还是先把她叫醒比较好。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "只要大声叫她的名字，或者用力摇晃她的肩膀，应该就能叫醒她了吧。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "明明这个时候只要大喊 “琴!伊!姐!” 就好了。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "但是当话语说出口的时候，却从大声的叫喊变成了小声的呢喃。 "

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "诺琪" "{size=20}\"琴伊姐……\""

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "不知道为什么，我能感觉到心脏扑通扑通跳个不停。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "琴伊姐的身体依旧有规律地微微起伏着。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "淡紫色的长发像波浪一样柔软，顺着完美的身形披散下来。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "柔和的灯光在桌面上跳动着，整个屋子都染上了温暖的色调。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "灯光下，披垂在她的身体上的长发透射出了明亮的金色光晕，如同神话中美丽的女神。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "琴伊姐嘴角微微翘起，一脸幸福的样子。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "摆动着的，长长的睫毛为她本就无比美丽的脸更添了一份楚楚动人，而微微翕动的嘴唇更像是在渴求着些什么。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "这还是我第一次如此近距离看到她的睡颜。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "大部分时候，琴伊姐都是以一个可靠大姐姐的形象出现在我面前。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "仿佛总是她在前面，用温柔的微笑引导着我。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "现在我却很难把眼前这个少女和她联系在一起。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "我的心跳得更猛了。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "真是奇怪啊，一般来说人无法感受到自己的心跳吧。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "为什么心脏跳得这么快呢……"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "不知不觉间，我已经伸出了一根手指，凑到了琴伊姐面前。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    "顿了一下，然后轻轻戳了一下她的脸颊。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "（戳~）"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    J "嗯~"

    "琴伊姐终于有了反应，她的睫毛和嘴唇动了动，发出了小猫一样的可爱声音。"

    "这一戳对她并没有什么效果。"

    "但对我的理智来说确是毁灭性的打击。"

    ## CG逐渐开始淡出，画面变白
    scene white
    with dissolve

    "那个时候，我确实察觉到了事情不太对劲，但是身体更快地做出了行动。"

    "在我反应过来之前，我的意识就已经停滞了。"

    "那一个瞬间，整个世界似乎都成为了空白。"

    "只剩下了我和她两个人。"

    "我也闭上了眼睛。"

    scene black
    with dissolve

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "琴伊姐的脸颊……好软……"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    "当嘴唇上传来了温暖的触感时，我才意识到发生了什么。"

    "——我亲了她。"

    "这份温存是那么美好，那么甜美，那么令人感到幸福。"

    "如果可以的话，我真的希望这一瞬间能永远地持续下去……"

    scene cg5_1

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "啊啊啊我在干什么!"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    "我的意识终于回到了现实世界。"

    "现实世界中发生的所有事情一股脑地冲进了我的脑袋，让我陷入了无比的混乱。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "呜!"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    "我立刻飞身后退。"

    "在撞倒了一把椅子后，又重重地撞上了书柜，几本书摇摇晃晃地掉了下来。"

    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "啊!疼!"
    show noki 20 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    scene cg5_2
    with dissolve

    show jean 15 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    J "唔……诺琪?"
    show jean 15 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    "琴伊姐也缓缓睁开了紫色的眸子，双唇微张，以迷蒙的睡眼望着我。"

    hide jean
    show noki 11 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    pause 0.5
    show noki 17 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "啊哈哈琴伊姐刚才您好像不小心睡着了我看您好像还在研究途中就把您叫醒了如果打扰到您休息了我十分抱歉"
    show noki 15 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    N "我真的只是把您叫醒了其他什么都没有做啊啊啊"

    show noki 15 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    N "就这样那什么希望你能喜欢我做的饮料再见祝您研究顺利"
    show noki 15 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    hide noki

    show jean 14 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve
    J "…?"
    show jean 14 onlayer overlay:
        xpos -170
        ypos 700
    with dissolve

    hide jean
    scene black
    with dissolve

    "没有等琴伊姐做出反应，我就飞快地夺门而出。"

    "身体轻飘飘的，嘴唇上还残留着刚才的余韵，宛如梦境一般。"

    return
