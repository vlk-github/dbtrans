/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50173
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2017-05-03 17:24:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for test_1
-- ----------------------------
DROP TABLE IF EXISTS `test_1`;
CREATE TABLE `test_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `summary` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of test_1
-- ----------------------------
INSERT INTO `test_1` VALUES ('1', '\r\n五一全国接待游客1.34亿人次 3天花791亿', '4月30日，“五一”假期第二天，各地迎来客流高峰。图为游客经过李世民亲封的“天下第一名刹”牌坊。');
INSERT INTO `test_1` VALUES ('2', '特朗普称若情况允许愿与金正恩会面 白宫:目前不行', ' 美国总统特朗普5月1日接受美国媒体采访时表示，如果情况允许，他愿意与朝鲜最高领导人金正恩举行会面');

-- ----------------------------
-- Table structure for test_2
-- ----------------------------
DROP TABLE IF EXISTS `test_2`;
CREATE TABLE `test_2` (
  `id` int(11) NOT NULL,
  `content` text CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of test_2
-- ----------------------------
INSERT INTO `test_2` VALUES ('1', '<div class=\"text\" id=\"text\" style=\"font-size: 14px;\">\r\n<p align=\"center\" style=\"font-size: 14px;\"><img src=\"http://himg2.huanqiu.com/attachment2010/2017/0502/20170502071500603.jpg\"></p>\r\n<p style=\"font-size: 14px;\">　　4月30日，“五一”假期第二天，各地迎来客流高峰。图为游客经过李世民亲封的“天下第一名刹”牌坊。 王中举 摄</p>\r\n<p style=\"font-size: 14px;\">　　中新社北京5月1日电 (记者 周音)<a href=\"http://country.huanqiu.com/china\" class=\"linkAbout\" target=\"_blank\" title=\"中国\">中国</a>国家旅游局5月1日披露，“五一”三天假期，中国共接待游客1.34亿人次，同比增长14.4%，实现旅游总收入791亿元人民币，同比增长16.2%。</p>\r\n<p style=\"font-size: 14px;\">　　国家旅游局新闻发言人侯振刚当天在北京举行的新闻发布会上表示，2017年“五一”假期，中国各地旅游业从景点旅游模式走向全域旅游模式的转变态势明显。以往景区型产品逐渐被多样化的目的地产品所取代，园区型产品异军突起，各种新业态产品全面开花，乡村旅游、城市周边游、古城古镇游等产品持续火爆。</p><div class=\"ad250x250 fLeft marRig10\" id=\"adPp\"><!-- Ad Survey 广告位代码  文章内页画中画08--><script type=\"text/javascript\">AD_SURVEY_Add_AdPos(\"9263\");</script></div>\r\n<p style=\"font-size: 14px;\">　　此外，自驾游产品持续火爆。“五一”期间，城市周边乡村，自驾游客异常火爆，热门旅游活动项目赏花、采摘、游园等活动备受青睐。随着乡村旅游的深度开发、乡村旅游扶贫和美丽乡村建设的持续开展，乡村环境不断改善，走进乡村、品味农韵、回归自然成为市民假期首选。\r\n</p><p style=\"font-size: 14px;\">　　侯振刚指出，以往，假日经济繁荣的背后是热点景区接待人数超负荷、秩序混乱，冷门景区门可罗雀、经营惨淡。为此，国家旅游局实施全域旅游发展战略，全面加强大众旅游时代假日旅游管理。从2017年“五一”假日的市场秩序情况来看，全域旅游管理的理念和效用得到了有效检验。\r\n</p><p style=\"font-size: 14px;\">　　侯振刚说，节日期间，在国家旅游局引导下，各地多措并举应对人流高峰，强化公共服务保障游客出行。针对可能出现的重点景区游客爆满，安全保障压力加大等特点，国家旅游局要求各地落实景区景点游客承载量监控，倡导通过各种渠道预约游览，及时广泛发布安全预警信息，做好高峰时段游客的疏导控制。\r\n</p><p style=\"font-size: 14px;\">　　侯振刚强调，国家旅游局正在从封闭的旅游自循环，向开放的“旅游+”融合发展方式转变，“旅游+”正以强大活力与其他产业磨合、融合、组合，不断衍生新产品、新业态、新供给。\r\n</div>');
INSERT INTO `test_2` VALUES ('2', '<div class=\"text\" id=\"text\" style=\"font-size: 14px;\">\r\n                        <p style=\"font-size: 14px;\">　　中新社华盛顿5月1日电 <a href=\"http://country.huanqiu.com/america\" class=\"linkAbout\" target=\"_blank\" title=\"美国\">美国</a>总统特朗普5月1日接受美国媒体采访时表示，如果情况允许，他愿意与<a href=\"http://country.huanqiu.com/north_korea\" class=\"linkAbout\" target=\"_blank\" title=\"朝鲜\">朝鲜</a>最高领导人金正恩举行会面。</p>\r\n<p style=\"font-size: 14px;\">　　特朗普当天在白宫椭圆办公室接受彭博社专访时做出上述表态。特朗普说，“如果与他(金正恩)会面是一件可行之事，我肯定会这么做，并且会感到荣幸，但前提是情况要允许。”他说，“大多数政治人物不会明确表态愿意与金正恩会面，但我愿意。”</p>\r\n<p style=\"font-size: 14px;\">　　特朗普在采访中没有指明“情况允许”的具体含义。这一表态也成为当天白宫例行记者会上的热门话题。</p><div class=\"ad250x250 fLeft marRig10\" id=\"adPp\"><!-- Ad Survey 广告位代码  文章内页画中画08--><script type=\"text/javascript\">AD_SURVEY_Add_AdPos(\"9263\");</script></div>\r\n<p style=\"font-size: 14px;\">　　白宫发言人斯派塞1日表示，“情况允许”意味着很多事情，这首先需要朝鲜立即停止挑衅性行为。斯派塞说，朝鲜半岛局势持续紧张，朝鲜对美国以及地区盟友构成严重的潜在安全威胁。特朗普总统将始终把保护美国的国家安全作为首要目标。他强调，从目前的情况看，美朝领导人之间不存在会面的可能性。\r\n</p><p style=\"font-size: 14px;\">　　对于特朗普使用“感到荣幸”的措辞，斯派塞解释称，鉴于金正恩是朝鲜领导人，特朗普总统此言是出于外交层面的考虑。\r\n</p><p style=\"font-size: 14px;\">　　朝鲜半岛局势近期轮番升级。美军“卡尔·文森”号航母上月29日在朝鲜半岛东部海域与韩军举行联合演练。同日，朝鲜试射一枚导弹，但以失败告终。朝鲜问题现已成为特朗普政府面临的首要国家安全问题。特朗普近日多次就朝鲜问题发声。\r\n</p><p style=\"font-size: 14px;\">　　特朗普在接受路透社采访时表示，希望通过外交手段解决朝鲜问题。但他同时强调，与朝鲜发生大规模冲突的可能性是存在的。他对美国<a href=\"http://country.huanqiu.com/colombia\" class=\"linkAbout\" target=\"_blank\" title=\"哥伦比亚\">哥伦比亚</a>广播公司表示，如果朝鲜再次进行核试验，他将不会感到开心。当被问及美国是否会采取军事行动时，特朗普回答，“不知道，我们要再看看。”\r\n</p><p style=\"font-size: 14px;\">　　有消息称，美国会众议院本周将就是否对朝鲜施加新的经济制裁进行讨论。新一轮制裁可能针对朝鲜的航运业。(完)\r\n                    </div>');
