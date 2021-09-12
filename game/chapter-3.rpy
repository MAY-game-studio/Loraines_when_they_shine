define ch4_1 = Character("商人",what_prefix="\"",what_suffix="\"")
define ch4_2 = Character("糖果店老板",what_prefix="\"",what_suffix="\"")

image bg4_1:
    contains:
        "images/背景/小镇_白天.png"
        size(1920,1080)
image bg4_2:
    contains:
        "images/背景/小镇_黄昏.png"
        size(1920,1080)
image bg4_3:
    contains:
        "images/背景/黄昏.png"
        size(1920,1080)

label chapter_3:
    scene bg4_1
    with dissolve
#【加一段表示现在是下午俩人开始逛街的内心os】

    show jean 4:
        xpos 604
        ypos 80
    with dissolve
    J "您好，这个钟表……"

    ch4_1 "啊，两位美丽的小姐，在下很荣幸向您们介绍。如您所见，这个精美的钟表出自南方的特拉科潘工匠之手，他们那精湛的铁系魔法技艺即使是密涅瓦女神看了也要赞叹不已……"

    show jean 15:
        xpos 604
        ypos 80
    with dissolve
    J "嗯……是很有趣的装置呢。"

    ch4_1 "没错，这件完美的魔法工艺品完全值得称作是艺术品……这位小姐真是目光如炬，容我冒昧，您是魔法师吗?"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "那当然啦!琴伊姐可是这里最厉害……"

    show jean 17:
        xpos 200
        ypos 80
    with dissolve
    J "没有没有——"

    "琴伊姐急急忙忙地打断了我的话，看上去她并不想聊这个话题。"

    show jean 10:
        xpos 200
        ypos 80
    with dissolve
    J "请不要在意……您这个钟表多少钱?"

    ch4_1 "这位眼光敏锐的小姐，您可算是问对人了。要说这里谁最了解这个小玩意儿，那肯定是非我莫属。这家伙可不是个简单的钟表，里面的铁系魔法装置非常精妙，使它能够在不同的时间产生不同魔力流动形式……"

    "商人又开始滔滔不绝地赞美起他的商品了，似乎完全无视了琴伊姐的询问。"

    "说起来，这个人竟然不认识琴伊姐……莫非他不是小镇的本地人?"

    "…不如说，这种奇怪的说话方式肯定不也是本地人吧。"

    "应该是旅行到此处的游商。"

    "也难怪他会有来自南方那个特拉啥啥地方的钟表。"

    "……"

    ch4_1 "我向您保证，这家伙可是最精密的铁系魔法工艺品，不要说一年，就是十年，一百年，时间精密度也不会有哪怕1秒的差距……"

    ch4_1 "哦……我的天哪，我又说多了!您刚才问的是什么?哦，价钱的话，这件最精美的艺术品——我是说人类之手所能做出来的，只收您89枚银币——看在您也是位懂行的份上。"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "这也太贵了啊!!!"

    ch4_1 "哈哈哈，这位活泼的小姐，你可是说对了。这样一笔钱，即使放在那些最奢侈的贵族老爷手里，也够他们穷奢极欲一阵子了。但是，我敢和你打赌，这家伙绝对值这个价钱……"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "……我可以拿过来看看吗?"

    ch4_1 "当然没问题，交给您，我不能放心更多了。您是魔法——啊，我是说，这东西在您手里可比在我这种草帽手里妥帖得多了。只有识货的人，像您这样的，拿着它才有价值……"

    "那个旅行商人一边继续着他浮夸的说辞，一边把那台钟搬了起来，挪到了琴伊姐面前。"

    "那台小型座钟看上去就知道做工很精致，大小差不多相当于一本精装厚书。"

    show jean 1:
        xpos 200
        ypos 80
    with dissolve
    "琴伊姐把钟举了起来，仔细地检查了一下，似乎还用了一点魔力试探。"

    "虽然琴伊姐看得很认真，不过说真的……即使真的是非常精巧的魔法装置，这个价格也有点过高了。"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    "如果打个七折，可能还算是个正常偏高的价格。"

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    "89银币……也太离谱了。"

    show jean 5:
        xpos 200
        ypos 80
    with dissolve
    J "没问题。麻烦您帮忙包装一下，给个袋子。"

    show noki 11:
        xpos 901
        ypos 80
    with dissolve
    N "哇!"

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    "与我想象的不同，琴伊姐没有一丝的犹豫。"

    show jean 10:
        xpos 200
        ypos 80
    with dissolve
    J "这是钱……麻烦您清点一下吧，我也不确定够不够。"

    ch4_1 "啊哈，我想我们不需要这样做。那只是几枚硬币，也许我喝两天酒就花得一干二净了!"

    show noki 18:
        xpos 901
        ypos 80
    with dissolve
    "诺琪" "{size=20}\"但是，万一钱给多了怎么办……\""

    show jean 1:
        xpos 200
        ypos 80
    with dissolve
    "不过琴伊姐似乎并不在意，只是转过头来，对我安慰似地笑了一下。"

    "转眼间，琴伊姐就从商人手中接过了包装好的钟。"

    "随后我们就离开了这个奇怪商人的摊位。"

    scene black
    with dissolve
    scene bg4_1
    with dissolve
## 原地黑屏转场

## 诺琪出现

    show noki 4:
        xpos 604
        ypos 80
    with dissolve
    N "啊，那边是卖水果糖的欸!赶紧去看看吧!"

    show noki 3:
        xpos 604
        ypos 80
    with dissolve
    N "上次苹果味的卖光了可真是巨大的悲剧，这次不能再错过了!"

## 琴伊立绘出现

    show noki 3:
        xpos 204
        ypos 80
    with dissolve

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "啊——你…"

    "我拽着看上去一脸不情愿的琴伊姐，快步冲向了糖果店。"

    show noki 12:
        xpos 901
        ypos 80
    with dissolve
    N "老板，苹果味的硬糖还有吗?"

    ch4_2 "喔，还多着呢。"

    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "太好了!给我多来点!"

    ch4_2 "好嘞!"

    "糖果店老板撑开了一个纸袋，然后从糖果堆里掏出了一把铲子，铲起了满满一整铲糖果。"

    ch4_2 "这么多，够吗?"

    show noki 16:
        xpos 901
        ypos 80
    with dissolve
    N "不够不够，再来点。都要苹果味的。"

    ch4_2 "得嘞!"

    "老板把一整铲糖果都倒进了撑开的纸袋里。"

    "随即又铲起了一堆糖果，这次差不多有大半铲左右。"

    ch4_2 "加上这些够吗?"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "嗯……应该差不多了，要不再稍微来一点吧。"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "……"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "我先声明，我不吃糖。"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "啊，我知道。"

    show jean 17:
        xpos 200
        ypos 80
    with dissolve
    J "……"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "你一个人能吃完这些?"

    show noki 13:
        xpos 901
        ypos 80
    with dissolve
    N "当然可以啦!这些也没多少吧。"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "真的没多少吗……纸袋已经快装不下了。"

    show noki 3:
        xpos 901
        ypos 80
    with dissolve
    N "哎呀~肯定可以吃完的，琴伊姐可不要小看我啊~"

    show jean 16:
        xpos 200
        ypos 80
    with dissolve
    J "嗯，这确实是一件很值得骄傲的事情呢。"

    show noki 15:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊……姐?"

    "感觉到了一丝凉意。"

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    N "啊哈哈哈……这个，其实我想的是，能买到也不容易，不如就一次性多买一点啦。"

    show noki 17:
        xpos 901
        ypos 80
    with dissolve
    N "这些我当然是要吃很久的啦——"

    show jean 12:
        xpos 200
        ypos 80
    with dissolve
    J "原来是这样吗——那这些糖果，我们的诺琪同学能吃多久呢?"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "让我想想……大概也许能吃两三周?"

    show jean 16:
        xpos 200
        ypos 80
    with dissolve
    J "哇，两三周，有这么久啊。"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "啊哈哈哈……也可能是一周吧……"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "以我对你的了解，买多少都只能撑过两天。"

    show jean 18:
        xpos 200
        ypos 80
    with dissolve
    J "一旦开始吃，就绝对停不下来了。"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "啊，其实我常常怀疑你心理年龄是不是只有十岁。"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "啊啊啊好好好——"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "吃糖也是一种爱好嘛…"

    show noki 20:
        xpos 901
        ypos 80
    with dissolve
    N "什么嘛!竟然说我像小孩子!"

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    N "为了向琴伊姐证明我还是有着很好的约束力，还是忍痛去掉了一半的硬糖。"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "嗯，三周吃完，肯定不提前。"

    scene black
    with dissolve

    scene bg4_3
    with dissolve

    "太阳逐渐落下，隐没在了小镇层层叠叠的房屋之后。"

    "即使即将沉入大地，夕阳也依然释放着璀璨的橘红色光芒。"

    "照亮了附近的云层，以及大半个天空。"

    "和琴伊姐一起采购的时光飞速逝去，转眼间已经是黄昏了。"

    "渐渐的，我们的采购从寻找各种需要或者有意思的商品，变成了漫无目的、悠哉悠哉的散步。"

    "对我来说，这真的是最美好的时光。"

    "抛开一切事情，只是单纯地享受和琴伊姐一起散步。"

    "真希望这样的时光能一直持续下去啊……"

    scene bg4_2
    with dissolve

    show noki 9:
        xpos 604
        ypos 80
    with dissolve
    N "……那个奇怪的商人还在啊。"

    "修辞浮夸的旅行商人依然待在他的摊位上。"

    "他也看到我们转了一圈回来，向我们招了招手，我也微微挥手回以致意。"

    show noki 4:
        xpos 604
        ypos 80
    with dissolve
    N "说来，琴伊姐真的好喜欢这个钟表啊。"

    show noki 12:
        xpos 604
        ypos 80
    with dissolve
    "即使价格那么贵，也还是买了回来。"

    show noki 12:
        xpos 901
        ypos 80
    with dissolve
    show jean 9:
        xpos 200
        ypos 80
    with dissolve
    pause 1
    show jean 1:
        xpos 200
        ypos 80
    with dissolve

    J "这个……这个钟表确实是不便宜，但是它也有着独特的有趣之处。"

    show noki 3:
        xpos 901
        ypos 80
    with dissolve
    N "我知道我知道~琴伊姐是比较喜欢前沿魔法装置嘛"

    show jean 5:
        xpos 200
        ypos 80
    with dissolve
    J "嗯……虽然肯定没有他宣传的那么夸张，但是这个钟表确实是非常精美的。"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "啊，我记得那个人说过，好像是来自南方的特斯啥啥……总之似乎是个特别善于制作铁系魔法工艺品的地方。"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "是特拉科潘啦，想不到你竟然还记得。"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊姐听说过这个地方吗?"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
    J "嗯……我也不太清楚。"

    show jean 11:
        xpos 200
        ypos 80
    with dissolve
    J "就像你说的，那里好像铁系魔法技术非常发达，也有着相当的历史渊源。"

    show noki 19:
        xpos 901
        ypos 80
    with dissolve
    pause 0.5
    show noki 12:
        xpos 901
        ypos 80
    with dissolve
    N "是嘛，铁系魔法，铁系魔法…"

    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "咱们啥时候学铁系魔法?"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "你手头的都学不明白呢，还想多学啊?"

    show noki 14:
        xpos 901
        ypos 80
    with dissolve
    N "诶——因为听起来有趣啊!"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "要是现在学的是铁系魔法说不定我就能学明白了。"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "你啊你啊……"

    hide noki
    with dissolve
    hide jean
    with dissolve

    "……"

    "我和琴伊继续在夕阳下漫步。"

    "在橙红色的光芒下，商贩们陆陆续续地收拾东西离开了。"

    "不知不觉中，我们再次走到了那个旅行商人的摊位前。"

    "他似乎也要收拾东西离开了。"

## 两个人立绘出现（原位）
    show noki 9:
        xpos 604
        ypos 80
    with dissolve

    N "老板，特拉可……就是那个钟表的产地是在什么地方啊?"

    show noki 7:
        xpos 604
        ypos 80
    with dissolve

    N "那里的人制作铁系魔法装置很厉害是吗?"

    ch4_1 "啊，原来是这位活泼的小姐。我猜你说的是特拉科潘吧，那可是一个真正的大城市。就如你所说，那里制作铁系魔法装置的工艺非常出名。"
    show noki 7:
        xpos 901
        ypos 80
    with dissolve

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "我听说……那一片的魔法制品都是禁止往外出售的，这是怎么一回事?"

    ch4_1 "这位眼光敏锐的小姐，您说的确实不错。不过这都是以前的事啦，大概在几年前，战争结束之后，禁令就取消了。我去年在那里旅行的时候……"

    "滔滔不绝的旅行商人和沉默的琴伊姐又聊了起来。"

    "主要内容似乎是商人去年在南方旅行时的一些见闻。"

    "琴伊姐还在礼貌地等待着对方说完，但我已经不想再听下去了。"

    show noki 18:
        xpos 901
        ypos 80
    with dissolve
    N "唉……我就不该来问……*小声"

    show noki 19:
        xpos 901
        ypos 80
    with dissolve
    "百无聊赖的时候，我随便看了看尚未收拾完的店铺里摆放的东西。"

    "大部分都是一些外地生产的手工业产品。"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    "既有像魔法钟表那样的精密产品，也有很多呢绒之类的日用品原材料。"

    "除此之外，也有一些书籍，但都是用我不认识的文字写成的。"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N"唔?这是……?"

    "在大堆的人工产品之中，摆放着一只干枯的花。"

    "我把花轻轻拿了起来。"

    "它看上去并不像是任何我见过的品种。"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "嘛……毕竟这是个旅行商人的铺子，大概又是某个远方的偏僻地方特产的植物吧……"

    "我凑上去闻了闻，虽然花已经风干了，但是依然能闻到淡淡的香气。"

    ch4_1 "喔，瞧瞧这位小姐发现了什么。这是在南方很常见的一种花，据说能让人心情平静。当地人经常用这种花做成饮料喝，它的名字就叫做……额，叫做……"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "……洛兰花。"

    ch4_1 "对对对，瞧瞧我这记性，是叫洛兰花。看来这位目光敏锐的小姐不仅目光敏锐啊，还是一位博学的学者呢。"

    show jean 9:
        xpos 200
        ypos 80
    with dissolve
    J "我只是偶尔听说过罢了……洛兰花有着独特的香气，花瓣可以用来泡茶，如果加入糖和蜂蜜会很好喝……"

    ch4_1 "这位小姐真是博学啊……这里还有风干的洛兰花瓣在出售，两位小姐要不要买一些回去呢?"

    "商人在他已经收拾起来了的一堆货物里翻找，最终掏出了几个大包。"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "诺琪……我看一下整朵的那支花。"

    show noki 19:
        xpos 901
        ypos 80
    with dissolve
    N "啊!好的。"

    "我伸手把刚刚在摊位上捡到的那支洛兰花递给了琴伊姐。"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "已经干枯了啊……也是，毕竟这一朵是从那么远的地方一路带过来的。"

    "琴伊姐从我手中接过了花，把它拿到眼前端详了起来。"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
    J "……"

    "我认真地盯着琴伊姐，但是她只是面无表情地盯着花朵，不时用手指旋转一下花柄。"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊姐?"

    show jean 17:
        xpos 200
        ypos 80
    with dissolve
    pause 1
    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "啊!没什么……算啦，我们北方人大概是喝不惯这种饮料的。"

    show noki 12:
        xpos 901
        ypos 80
    with dissolve
    N "诶……听起来很新奇啊，不想尝尝看嘛?"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "而且感觉琴伊姐好像对洛兰花很熟悉的样子…?"

    show jean 9:
        xpos 200
        ypos 80
    with dissolve
    "没有啦，我只是以前看书的时候碰巧读到过一些描述……我也是第一次见到实物。"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    "我只是好奇罢了……毕竟是生长在很远地方的花，而且能泡茶的花也很少见对吧。"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    "好啦——总之现在也不早了，早就到该吃晚饭的时候了，我们走吧。"

    "琴伊姐轻轻把花放下，向老板点头致谢，然后拎起东西就准备离开。"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "——她大概还真的从来没有过如此喜欢过什么东西。"

    "追溯到上一次看到她这种眼神应该还是……哦，那个钟表。"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    "但洛兰花明明和魔法没有关系?"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "等等!老板，这些干花瓣我都要了!"

    "我掏出了口袋里所剩不多的钱，一股脑塞给了那个奇怪的旅行商人。"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "诺琪……"

    show noki 1:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊姐别管啦~我就是想尝尝看新东西嘛。"

    ch4_1 "两位小姐不用担心，我敢保证，这里绝对没有假冒产品，因为所有这些货物都是被我亲自带过来的。"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    "……"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
#    J "那你至少少买一些吧，万一不好喝呢?"

    "琴伊叹气似地笑了一下，没有再说别的话。"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    "她默默地指挥商人装好了花，然后把找零交给了我。"

    scene black
    with dissolve
    scene bg4_2
    with dissolve

    "我们告别了那个旅行商人，拎着大大小小的包，并肩走在街道上。"

    "几乎所有的商贩都已经离开了，商店也大多闭上了门。"

    "夕阳照射着我们脚下的路，将逐渐变得冷清的街道染成了橘红色。"

    show jean 4:
        xpos 604
        ypos 80
    with dissolve
    J "今天已经比较晚了，就不要再做饭了，在外面吃吧。"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    pause 1
    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "嗯……?嗯，好。"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "东西这么多，要不要先回去放一趟?"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "……"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
    J "嗯，好。"

    hide noki
    with dissolve
    hide jean
    with dissolve

    "在橘红色的天空下，建筑的影子都拖得长长的，染上了黄昏金黄色的光晕。"

    "我们两个人的影子也拖得长长的，在金黄色的路面上一起摇晃着。"

    return
