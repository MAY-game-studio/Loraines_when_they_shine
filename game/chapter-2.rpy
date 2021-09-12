image bg3_1:
    contains:
        "images/背景/野外.png"
        size(1920,1080)

image bg3_2:
    contains:
        "images/背景/晴天.jpg"
        size(1920,1080)


label chapter_2:
    scene bg3_1
    with mytrans1
### 两个人立绘出现，有传送的特效
    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "呼——"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "还不太习惯传送魔法吗?"

    show noki 12:
        xpos 901
        ypos 80
    with dissolve
    N "没有啦——"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "毕竟已经传送过这么多次了。"

    "清晨的阳光铺在郊外的大地上，也落在了我们身上。{color=#f00}大段心理描写演出效果实在拉跨，建议更改q"

    "现在离中午还有很长一段时间，所以并不是很热。"

    "这里就是我们平时练习魔法的场地。"

    "因为可能会练习一些有破坏性的魔法，在城里会比较危险。"

    "而这里在人烟稀少的郊外……即使不小心炸掉了一棵树之类的也没关系。"

    "路程上来说，这里离小镇里的店铺也不远。"

    "如果用魔法传送过来，更是一瞬间的事情。"

    "此外，这里还有一间无人居住的小屋，累的时候可以休息。"

    "——总之是再适合不过了。{color=#f00}世界观不该这么铺吧，这是最笨的方式了"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "还不是为了照顾你，一到了中午就懒得动不了了……"

    show jean 11:
        xpos 200
        ypos 80
    with dissolve
    J "就算是从店铺走路过来，其实也只要半个小时，就当是早上活动一下身体了。"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "这可不行，快到中午的时候，每过半个小时，可是要热一大截的!"

    "现在天气还不是很热，但是随着临近中午，室外会变得越来越难以忍受。"

    "为了抓住中午之前的宝贵时间来练习魔法，一般我们都会用魔法直接传送过来。"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "诶呀——不说这个了~"

    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊老师，我们今天学什么呢?"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
    J "咳咳……"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "啊……好的，好的"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊姐琴伊姐~"

    "虽然生活在一起，年龄也相差不大……{color=#f00}这里直接陷入回忆合适吗。。而且字太多了吧q"

    "但是实际上，我在魔法事务所里属于晚辈，在这里学习魔法。"

    "而琴伊姐是我的老师，也是这家事务所的店主。"

    "不过琴伊姐总是不喜欢我叫她老师。"

    "每次我问她原因的时候，她总说这个称呼太显老了。"

    "这样当然也说得通……不过我记得，我第一次叫琴伊姐老师的时候，她不是这么说的。"

    "那还是在我们刚刚见面，也就是她从我的上一位老师那里继承这个事务所那会儿。{color=#f00}同理，不在赘述q"

    scene white
    with dissolve
    scene bg3_2
    show MemoryFilter

    N "呃，我大概可以称呼您为，琴伊老师……吗?"

    J "老师……"

    N "啊……您不喜欢这个称呼吗?"

    N "我完全不介意直接叫名字的哈哈哈…就是这个……"

    J "啊，不，没什么。"

    J "请别在意。"

    scene white
    with dissolve
    scene bg3_1

    with hpunch

    show jean 16:
        xpos 200
        ypos 80
    with dissolve
    J "诺琪!别走神啦!"

    show noki 11:
        xpos 901
        ypos 80
    with dissolve
    N "哦呀…!"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "今天就练习感知和控制气流的魔法操作吧。"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "啊……好的!"

    show jean 5:
        xpos 200
        ypos 80
    with dissolve
    J "如果只是制造出风，你应该已经没问题了。"

    show jean 10:
        xpos 200
        ypos 80
    with dissolve
    J "不过，操纵气流的魔法，最困难也是最重要的地方就在于精细的控制。"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N"比如说早上减轻锅重量的那个魔法?"

    show jean 11:
        xpos 200
        ypos 80
    with dissolve
    J "是的，对气流的精细控制。"

    J "按照昨天讲的，你还记得是怎么用魔法操控空气的吗?"

    show noki 19:
        xpos 901
        ypos 80
    with dissolve
    N "我想想……嗯……"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "大概……主要是……向空气中注入魔力，从而感受到它们如何流动?"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "好像、差不多、是这样?"

    show jean 1:
        xpos 200
        ypos 80
    with dissolve
    J "嗯，可以看出来你确实记下来了一些，但是昨天讲的并不是这样的。"

    J "并不是单纯地向空气注入魔力，而是让自己的魔力自发地流入进去。"

    show jean 11:
        xpos 200
        ypos 80
    with dissolve
    J "通过这种方法，让感知觉和气流之间产生共鸣。"

    J "魔力不会自发的从少的地方流向多的地方，而非自发的过程也肯定伴随着魔力的消耗。"

    show jean 5:
        xpos 200
        ypos 80
    with dissolve
    J "如果强行注入，很可能产生后一种的情况，会对气流产生较大扰动，导致得不到任何有效信息。"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "另外，因为人类没有天生感受体外魔力的感官机能，所以必须先设想出操控气流的感觉，不能只依靠感觉……"

    show noki 15:
        xpos 901
        ypos 80
    with dissolve
    N "啊……嗯……好的……"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "额……你听懂了吗?"

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    N "啊……这个……"

    show jean 16:
        xpos 200
        ypos 80
    with dissolve
    J "没听懂?"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "呃…就快听懂了!"

    "每次说到关于魔法的事情的时候，琴伊姐就像变了一个人一样，可以滔滔不绝地讲很久。"

    "虽然大部分我都能差不多听懂，但是很多时候真得很难跟上她的思路……"

    "不过我并不讨厌这样子，认真的人是最迷人的呢。"

    show jean 18:
        xpos 200
        ypos 80
    with dissolve
    N "啊~我是真的不太擅长这些抽象的理论啦!"

    show jean 9:
        xpos 200
        ypos 80
    with dissolve
    J "这样啊，那我再讲一……"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "啊等一下!"

    show noki 15:
        xpos 901
        ypos 80
    with dissolve
    N "我其实觉得，再讲一遍我也很难搞明白。{color=#f00}私以为此时琴伊应该变立绘q"

    N "要不我们就先开始练习吧!"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "就算有些细节现在不太清楚，大概也不太影响实际操作啦!"

    N "俗话说的好，实践出真知。"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    N "说不定练着练着就能搞明白了呢。"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "那……也行。"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "那就先试试吧。"

    with fade

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    N "诶~~~"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "还是不行呢……"

    show jean 1:
        xpos 200
        ypos 80
    with dissolve
    J "没关系的，别灰心。"

    show jean 11:
        xpos 200
        ypos 80
    with dissolve
    J "对魔力的精细操控本来就是需要反复练习才能掌握的技艺，刚开始不熟练很正常。"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "嗯……"

    show jean 14:
        xpos 200
        ypos 80
    with dissolve
    J "话说，你感觉更理解之前的理论了吗……尤其是关于魔力和感官的部分?"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "琴伊姐真的很在意理论欸……"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "只是应用的话，没必要那么较真吧~"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
    J "啊，我…"

    J "抱歉。"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "不不不不不，这没有什么要道歉的啦!"

    show noki 13:
        xpos 901
        ypos 80
    with dissolve
    N "呃…理论是应用的基础!对吧对吧"

    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "而且，我确实感觉理解更深刻了!"

    show jean 12:
        xpos 200
        ypos 80
    with dissolve
    J "嗯……"

    "琴伊姐好像不好意思地笑了一下……这是为什么呢?"

    show jean 13:
        xpos 200
        ypos 80
    with dissolve
    J "虽然大部分人应该都是这样看待魔法师的。"

    J "但是我想，魔法师应该并不只是“魔法用得很熟练的人”。"

    J "魔法是我们看世界的一面透镜。"

    show jean 5:
        xpos 200
        ypos 80
    with dissolve
    J "借助这面透镜，我们能够更清晰地看见这个世界……看到更细致、更美丽、更多的风景。"

    J "我们也能够创造出新的魔法，甚至是一些在以前看来难以想象的魔法……"

    J "在未来或许都是能够实现的。"

    J "在列虎·文克用光系魔法发明显微镜之前，谁敢相信我们可以看到比我们小那么多的生物?{color=#f00}这个点也不能用吗。。我属实也没有想到q"

    J "在阿朗斯特姆登上月球之前，谁又能想到这是区区火系魔法能够做到的呢?"

    show jean 4:
        xpos 200
        ypos 80
    with dissolve
    J "啊……我好像又开始自说自话了。"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    N "每次说到魔法研究的事情，琴伊姐就变得好认真啊……"

    N "感觉整个人的画风都和平时不一样了。"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "啊……是这样吗……"

    show noki 1:
        xpos 901
        ypos 80
    with dissolve
    N "不过，这样的琴伊姐，我也很喜……我觉得也很好啦!"

    show jean 17:
        xpos 200
        ypos 80
    with dissolve
    N "诶…?"

    show noki 9:
        xpos 901
        ypos 80
    with dissolve
    N "啊啊啊——没啥没啥，就是……"

    show noki 7:
        xpos 901
        ypos 80
    with dissolve
    pause 0.5
    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "说到创造新的魔法，我有一个想法!{color=#f00}同之前。。技术问题，我想想办法吧q"

    show jean 1:
        xpos 200
        ypos 80
    with dissolve
    J "嗯，你说。"

    show noki 8:
        xpos 901
        ypos 80
    with dissolve
    N "既然……不能把魔力强行注入空气，是因为会形成扰动……"

    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "那是不是可以把魔力注入其他人的体内，从而使用出超出一个人魔力量的魔法?"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "……"

    show jean 15:
        xpos 200
        ypos 80
    with dissolve
    J "人的魔力都是有上限的。"

    J "两个人的魔力也会产生很强的排斥。"

    J "……所以传递魔力需要额外付出极大的能量，实践上这是不可能的。"

    J "另外，如何使用别人的魔力也是个很大的问题。"

    show jean 3:
        xpos 200
        ypos 80
    with dissolve
    J "这一点我们之前上课的时候也说过……"

    show noki 5:
        xpos 901
        ypos 80
    with dissolve
    N "呃……"

    "虽然说过，但我大概可能好像也许是忘了?"

    show noki 15:
        xpos 901
        ypos 80
    with dissolve
    N "啊我…知道，应该是……"

    show noki 6:
        xpos 901
        ypos 80
    with dissolve
    N "额，我其实想的是……"

    "快转起来啊我的脑子!"

    "……"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    "啊，有了。"

    show noki 10:
        xpos 901
        ypos 80
    with dissolve
    N "那是不是把一个人的魔力清空，就可以做到了?{color=#f00}琴伊立绘换否q"

    N "既没有排斥，也可以自发。"

    show noki 1:
        xpos 901
        ypos 80
    with dissolve
    N "好耶，我可真是个小天才。"

    show jean 8:
        xpos 200
        ypos 80
    with dissolve
    J "……"

    J "嗯…"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "这倒是个很有趣的想法……"

    show jean 11:
        xpos 200
        ypos 80
    with dissolve
    J "确实有可能绕开魔力上限和排斥的问题。"

    "琴伊姐竟然表示了同意!"

    show noki 4:
        xpos 901
        ypos 80
    with dissolve
    "难道说……我瞎猫碰到死耗子了?"

    show jean 1:
        xpos 200
        ypos 80
    with dissolve
    J "不过魔力的排斥是非常非常强烈的，我也不确定是否可行。"

    show jean 6:
        xpos 200
        ypos 80
    with dissolve
    J "清空魔力带来的副作用和控制外来的魔力也都是不好解决的问题……"

    show noki 3:
        xpos 901
        ypos 80
    with dissolve
    N "这样啊，看来琴伊姐也需要时间研究一下呢……那今天的训练不如就……"

    show jean 7:
        xpos 200
        ypos 80
    with dissolve
    J "哒咩。"

    show jean 16:
        xpos 200
        ypos 80
    with dissolve
    J "你就别想着偷懒啦!"

    scene bg3_2
    with dissolve

    "虽然从结果来看是好的"

    "但是对于我（们?）这种只是把魔法当作生活工具的人来说，"

    "还是非常不理解为什么要搞这么多复杂的理论啊!"

    with hpunch
    "为什么啊!{color=#f00}屏幕抖动是我额外加的"

    return
