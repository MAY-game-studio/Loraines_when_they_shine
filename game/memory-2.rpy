define ch6_1 = Character("少女",what_prefix="\"",what_suffix="\"")
define ch6_2 = Character("偷袭者",what_prefix="\"",what_suffix="\"")

image bg6_1:
    contains:
        "images/背景/夜晚森林_月光.png"
        size(1920,1080)

image bg6_2:
    contains:
        "images/背景/夜晚森林_照明.png"
        size(1920,1080)

image bg6_3:
    contains:
        "images/背景/夜晚森林_黑暗.png"
        size(1920,1080)

image bg6_4:
    contains:
        "images/背景/夜空.jpg"
        size(1920,1080)

image bg6_6:
    contains:
        "images/背景/黑夜.png"
        size(1920,1080)

image bg6_7:
    contains:
        "images/背景/放大.png"
        size(1920,1080)

image bg6_5:
    contains:
        "images/背景/tmp.png"
        size(1920,2160)

transform trans6_1:
    pos(0,0)
    linear 0.2 pos(0,-1080)

label memory_2:

    scene bg6_1
    with dissolve

    "寂静的月光穿过了树叶的缝隙，照射在了这片土地上。"

    "夜晚的林间小路被掩盖在了朦胧的黑暗中。"

    "森林是沉默的，只能不时听到树叶被风吹动的声音。"

    "我放松地在树木间穿梭。"

    "即使偶尔踩碎了地上的落叶或枯枝，响声也很快就消散在了清风中。"

    ch6_1 "这里真是个适合偷袭的地方呢。"

    ch6_1 "光线这么暗，无论是躲在树后面、还是藏在草丛里，应该都很难被发现。"

    "少女" "{size=40}\"几位觉得是不是这样呢? \""

    "四周寂静无声，只有吹动着树叶的微风回答了我的问题。"

    "但是魔力的感应应该是不会有错的。"

    "这已经是我在逃亡路上遇到的第三次偷袭了。"

    ch6_1 "{i}synechia aktina ecosynchronize fos deca!"

    scene bg6_2

    "我把魔力汇聚到指尖，释放出了耀眼的光芒。"

    "强烈的光瞬间驱散了周围的黑暗，也刺得我有些睁不开眼来。"

    "嗖——"

    with vpunch

    ch6_1 "唔!!!"

    "回应我的是3支沉默的弩箭。"

    "少女" "{size=20}\"好险……\""

    "这三支箭都来自视野的盲区。"

    "其中一支背后射来的箭，几乎就是擦着耳朵飞过去的，惊出了我一身冷汗。"

    "对方大概是打算趁我用魔法照明，因为太刺眼而分神的一瞬间发动偷袭。"

    "少女" "{size=20}\"糟糕了……看来这次的人不好对付啊。\""

    "能躲开这几支箭，并不是因为我反映敏捷，更不是因为偷袭者射偏了。"

    "只是我为了以防万一，用魔法提前在身体周围布下了空气墙。"

    "空气墙轻微扭偏了箭的方向，我这才逃过一劫。"

    "少女" "{size=20}\"幸亏我早有准备……\""

    "我赶紧继续注入魔力，加厚了空气墙。"

    "想不到弩箭的穿透力这么强，下次不能再吝惜魔力了。"

    "还好提前探测到了有埋伏，有了一些防备……要不然这次就危险了。"

    "少女" "{size=40}\"出来吧，几位!\""

    "在大功率的照明魔法下，有几个人的身影已经可以隐约看见了。"

    "然而，没有一个人回答我，更没有人站出来。"

    "少女" "{size=40}\"悬赏金有多少，我可以给你们双倍。\""

    "——不可能的。"

    "能从城里逃出来已经是奇迹了，身上怎么可能还带着钱。"

    "不过这些偷袭者或许不知道这一点……这只是缓兵之计罢了。"

    "关键还是要赶紧找出所有埋伏着的人，然后吓退他们。"

    "逃亡的路上，很少能有休息和补给的机会，魔力非常珍贵。"

    "所以要尽量能避免交战，现在这种条件下，能节省任何一点魔力都好。"

    "传送魔法也要消耗太多魔力了，最好是能让他们知难而退。"

    "少女" "{size=40}\"你们也明白，干掉一个魔法师是非常困难的。\""

    "8个……9个……10个……"

    "少女" "{size=40}\"如果你们想要的不过是钱而已，那我们完全谈一谈。\""

    "11个……12个……能用魔力感应到的大约有12个人，只是不知道他们用的是什么武器。"

    ch6_2 "你能付给我们多少钱?"

    "在照明魔法的光芒下，一个男人从树后的阴影中跨出了半步。"

    "他并没有完全走出阴影，依然借着树干半遮半掩。"

    "不过依然可以看出来，他没有穿盔甲，服装也不是制服……大概不是纪律严明的正规军。"

    "还好……如果只是受到赏金诱惑的一群不法之徒，就有可能用魔法吓退他们。"

    "大概这个人是头领吧，至少先稳住对方再说。"

    ch6_1 "那当然是……呜!"

    "就在我回答的瞬间，一股无形的力量将我重重拍到了地上。"

    ch6_1 "该死的!有魔法师!是无声魔法!!!"

    "刚才那一下偷袭恐怕是奔着致命来的!"

    "好在我最后一刻感受到了魔力的流动，勉强躲开了……"

    "然而即使是余波，也有着巨大的威力，一下就把我推倒在了地上。"

    ch6_1 "不好，又来了!"

    "对方根本没有留下任何让人喘息的机会，立刻释放了第二次攻击。"

    "流动的魔力汇聚在一起，凝结成了尖利的长矛，空气也随之颤抖起来。"

    "此前释放出的空气墙被轻易地刺穿，每一滴魔力都发出了悲鸣。"

    "因为被第一次攻击打飞，摔倒在了地面上，现在我已经没有躲避的空间了。"

    scene bg6_3

    ch6_1 "呜!"

    "在攻击命中之前，我强行扭转了身体。"

    "魔法击中了身旁几寸远的地面，释放出剧烈的冲击波，再一次将我击飞。"

    "我在落叶和枯枝中翻滚着滑行了数米远，直到正面撞上了什么东西。"

    ch6_1 "呃啊……"

    "恶心和绞痛感一下子从胃里喷涌了出来，我好像吐出了一些东西，不知道是不是血。"

    ch6_1 "可恶……"

    "眩晕感挤满了整个脑袋，甚至无法分辨出地面在哪里。"

    "耳朵里只剩下嗡嗡的耳鸣声，眼睛也胀的发疼，什么都看不清。"

    "空气墙和照明魔法也无法维持了。"

    ch6_1 "不行……肯定还有第三次攻击……"

    "我挣扎着转过头来，睁开眼睛。"

    "就在这时，我终于看清了撞上的是什么东西。"

    "那是一个用黑布蒙住了半张脸的人。"

    "在黑暗之中，甚至看不清是男是女。"

    "唯一能看清的，只有蒙面黑布的缝隙里，没有一丝感情的冰冷目光；"

    "以及他手中，在那高高举起、即将落下的剑上，反射出的银白色月光。"

    ch6_1 "thellastia!"

    scene white
    with dissolve
    scene bg6_6
    with dissolve

    ch6_1 "呼——"

    ch6_1 "得救了……幸亏以前练过高速咏唱……"

    "我躺在地上，大口喘着粗气。"

    ch6_1 "差一点……差一点就没命了……"

    "在恢复了片刻后，我检查了一下伤势，施放了几个治疗魔法。"

    "万幸的是，伤势并不是非常严重。"

    "治疗魔法也很可靠，在耗费了不小的魔力之后，很快就恢复得差不多了。"

    "虽然最终依靠着高速咏唱的技术，我成功在剑砍到脖子上之前用传送逃离了出来。"

    "不过，如果不是最后恰好被打飞到了一个偷袭者同伙身边，让魔法师没法攻击……"

    "估计那个魔法师连高速咏唱的时间都不会留给我吧……"

    "恐怕我现在已经……"

    ch6_1 "……"

    "稍微休息了一会，在治疗魔法的效果完全发挥之后，我从地上爬了起来。"

    scene bg6_5 at trans6_1

    "这片森林非常大，即使传送了一次，也还在森林里面。"

    "不过根据我的估计，这里离刚才的战场已经很远很远了。"

    "即使那个魔法师能瞬移，也不可能在茫茫林海里找到我。"

    ch6_1 "唉……行李都丢光了，魔力也所剩无几了……"

    ch6_1 "今天肯定不能再赶路了，就在这里将就一晚上吧。"

    "我环顾四周，找了一棵比较粗的树，背靠在了上面。"

    scene bg6_7
    with dissolve
## 背景变化，聚焦左下角大树

    "这些人真的太可怕了，两次抓住了我分神的瞬间偷袭，每次都是致命攻击……*演出之后改"

    "真的差一点点就没命了……"

    ch6_1 "唉……我还一直想着怎么吓退对面，实在是太天真了……"

    "从服装来看，这些人应该只是被悬赏吸引的流寇。"

    "估计是在经过上一个城镇的时候发现的我……"

    ch6_1 "需要换一身衣服了……最好是能想办法改变一下容貌。"

    ch6_1 "罢了，先找到水和食物再说吧……"

    "明天可以去就近的城镇……后天可以去下一个城镇……"

    "但是不可能永远这样流亡下去，最后总要有一个落脚的地方。"

    "现在还有哪里能容得下我呢……"

    ch6_1 "……"

    scene bg6_3
    with dissolve

    "树林再一次恢复了沉默，只能听到清风扫过树叶的响声。"

    "我的意识也慢慢滑入了黑暗。"

    scene black
    with Dissolve(3)

    "然而那天晚上，就在我半睡半醒之时，"

    "飞驰的箭矢、爆裂的魔法、闪烁着寒光的利剑……突然带着恐怖的气氛从记忆中走了出来。"

    "这只不过是一个突然产生的幻觉，一个转瞬即逝的噩梦。"

    "当我被惊醒，重新抬起头环顾四周时。"

    scene bg6_1
    with dissolve

    "幻象已经消逝，周围的一切都恢复了安静的外表。"

    "月光也再一次穿过了树叶的缝隙，照射在了这片土地上。"

    "然而在我看来，森林的沉默从未如此冰冷，它的树荫从未如此阴郁，它的孤寂从未如此彻底。"

    return
