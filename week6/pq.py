#-*- coding: UTF-8 -*-
from gmpy2 import *
import time
N = [0x803F734ED9E3A3FBDEF8E3540B7B676FB66D15D2E5139840CB3CD06E62634C00A48EA2BF9BC3D7A709DBB47BE7E27DFB2C0E5B81254E6C326691471AE6DDC4A35539018BA6305DAFF1C480F195118B1310C546C31FE62C7AEC2A947013AC2897D00FD60E7B792DD499315341895BD1D1C9AA923E9373E1E01E2856B4FC8C6893L,0x845334AC0B3EB2239FDF0E3069750901E791CB774AD36941E30D85E5A0FED57749A30DC1F1F4CB191D9863F437C98293E8E8888B963BCF16B691F1D4EEF56C6807440E5FB5EC5B95DF3434DEDA30C60DCB4E77294BE027F984D5E675AEB1CBBE57E8CAF140226EAD6DCD9A9636A0CFF586FA434804CB09D7E8C48DE34EBE9049L,0x808627CED38A980D765454AC5DFEFC10195F6FEF9B35B52B742DBCE2419C34080A3EF3E9673FEA4DD629FF382155031EA6DCBA8372D42C1862F32B2BEE47E157FA7150C544635035F366F7D68234F56FA24180EB6A00A0F85C65AAEB455B8ED28F2285376CDA786F8C658CFEB3752F3504A7256EA3DBD22EEF20267D156FAB51L,0x8365D1FF23709FAAEF6330AECA9C848B292E0872C5C41E8CBE9D0780F32EBFC5FCC7947BD666F06AA619F952AFB8D7C08B9211960D1916235D8AB3A60DEC45B1EF5CC21848E56D5235717186EAD51AE22A5661BDFDC42E31F9181F6AB1D070FDEBB078A9980D7A0571B587130A1D3056CBA40CBBA287CD5031838BAB893B476BL,0x803F734ED9E3A3FBDEF8E3540B7B676FB66D15D2E5139840CB3CD06E62634C00A48EA2BF9BC3D7A709DBB47BE7E27DFB2C0E5B81254E6C326691471AE6DDC4A35539018BA6305DAFF1C480F195118B1310C546C31FE62C7AEC2A947013AC2897D00FD60E7B792DD499315341895BD1D1C9AA923E9373E1E01E2856B4FC8C6893L,0x8D41AC379635A2C8FFA55F609BE3EB6219C7AD0D3C335AC1F7AE27C3C0510E9ACDE319A6E00B891BDDB05C6B53F62E9321340BC0F19727C0526AC811CC02C7229241045A3D125978C1181264FDE49D8A148AAD8A8796C12C2AB5E8D7B0F98EDAC907C092B70D8B36E5BDC47C5801E4225BB508B1F081F5331C9B1324875EA25FL,0xD11B49BF43234D6595219AB7C21730DE0A13A7A01E63831A4D4F8DC5A7E68FCA0E9768EF0DABCAD036E08E17E4B27C1151DF364556D8F93D19565D9F40F095A49C6185F2630671EB5EC1EAA514BEC32D93A0F0459B52F1E34D4B9113413403F66619262EF1D3CBB025648C997CD1438DE21CFE4BEA0C6E00C72FFDE587929CB3L,0xDD1B58FF0DE86CD28DFFB60CC1EE0EFA3250D58264B3DA9CEAA5B5C17C728741F728C462C347DCB707BA7EE8672295F5A750C19D48AE23A32FC21E76F3188B85008E4EC1A66371BBB0825E558E876D80FA59E7099AF25B0B298131277E634772F24EE0ED1BACD3BA6F8D8E443D5AE16FAF6AA7DBAA59F91F763E4EAFD7D7F5CDL,0x9288E1EEF599EA72113D950723A8FC0ADD096C7312D8E78911FE64A4322C4FEC96FD70B345AA5A345481FB91D8549998A90E2429DCAF1EEEC863F396479A0BBD121E36B0EFAC8D002FC95B58B5879DD75251B5CEFCBE90BF50669742821BE2E89B3831FD6F0F3EAB310E5BF3FC66D702D5FF1581EE1DEFF161EFCA359063C6ABL,0x8B39E72D3C13D48F7773118B19F0D1A0CC592FD8FF12469E1D51ABA8869A23297CD62E28BCF885F744BD4A7C53CB5369F941F401EC010DA8665B7EB0B17B1839B3F0E49B51A266DDB84899EB302E050E43A284B5051C5B9002BA2B8BF1DD3A22C0BAB03A6E780F218852EE086F05E9ADF290189439AFF15986077D36D271C9A1L,0x85A0AC7E685995D9F8012C3A0249491956697997BBB6E5DDC1B53DC6184A843C3E4EB9B2D97FEAFAD097AA0FF640846287953C88F5A0813FD81FF3EBBDD62D66F4403653DCEC64ACE99F9FAAED4FD35513214EF4B4B9AA910E5923CD87F9330E3599F2CF1AD90EFC6BDABBD249D1AC8CF83836FE18399379E712010FC25A3DA3L,0x9FEDDC9C122AA836E9A04FE9358A118B358C7BC6F3ABDE4E035E2BCB15B52950DB1D23449EA62F83406FB591ED39564FD0E2DAD0954156037BB32C9C23C49DA83E2E85BC09A9B6FD75E2F55129044FA0F996895E8BF5E53D88938E4A3366649E97961BE5B7B4095476D013D2E9F6FE75DC21295747BF371AE346355A5ADBD93FL,0x808B8F96E7255B3F169EE854ABE0CD0AC7A4AE1B388CBC9A234E225842208A435842C254A55855B867F3FCA78E3887C8D1663B501A5D4D5E32F3EF84847F45651A5E2FC8A091E12E2B4DB7AB41113D258E2200FFB2BBF8B7C38B0049B3E2E60C65EB8B6375F03A40DC9F9AB01FEC60E09DC8CA3644A83738BDA0CFDB2B5ABB3DL,0x866AA521700CC11B537E0AA52D40843F8DD23469B9B4C5A3C966266DC9682947DA3A24B1505C932BD44EB3358290274F0BA295F9D40449B314531725BDB1DF55D57D088A5D188994C77362BFE54777D666B8C4D59C0C9C2B4D4E63780FD8D7C637444E0A9EC83A9ED3FA856D5155F6FCB5861F0CB66994EE0CCB615B99D22E73L,0xAAE5F7D640FD102E49217A08E0A4AF72EC895D5ABA020BEAF6F73053F4053D47CB7EBF3D583532ABFFF50F69508A4DBF2421742DCC2C16AE00E88C237653EC4DCFCD9A918763A9C9DE3CE3DA1FE2BC94FF93A9A7C261400A6E363C66816FDA0E44EE73662CFD2B8BFA926EF2B40F7D41F35B7E89516BC28330B5CF49976B8D7FL,0xD2611805B6839FD983F2C574BDAD1C50A4FB9FAB35F3BB643F90A9FBB0B84AF1D042E35E821564FCA783F1A2AF41349BB3E1C159B20EA6A0DB9E70597CB5C0780EF6CD78481AEAC0DF65A8DE35A8B5021FCE55332C5B2ADAEDCF80963BD6FFF773CAB55D73637C9BD667148FB1359782D38C41CBB43FA5FD56F424F842D8683DL,0x811F75BEAD6F0C3EA1560CFA4BFD4762F1DA3A30E22644AB16B1BEA5A6A1AF14F0C3C2E63865FD29241246C1473892232DAB6224AF1600F73340CBCA7BF5AF01EA1FA007E46064CE2F8DD92A9E7FA9F16CFEEE5A6CF67683BCD97F1E7E1BA73A9F86A8E4D7496393AC9727D10530A76B03B3A23321E8BDD756FCE265494F6D35L,0x9E52BAE97E34F02361E694ED55E87BC77ABAFB3124DC8DABFCCE71B51F1049CF3C22BC79B8841433CCB6DF840F2BD5A6E75A1CE52F54048FF4930E7B103C6A3433A2663BD9CBA0E38A35695F927EB2FF7A51939869A113D8A6CB03228C0E5D1466B1FF491129A988EFDBC636AB2610CAA50925554BE758321178F9EB94072C1DL,0x84FF95E263D30FAD83684CC08B11DAB54F5A0F3D24A8763C47B57750ED2E342022652836E2EBB30A765DC7364F417E4555D1FD72D140EFB72E283007028CC2A4FE97E4FE3B5D272C917E734F8715A0C5BFF2900640D8097425AFA965F9B1566F339F155ACEB59EDE241327813C920A6FB98A6BB9209379F1BBEBCC955949D8BBL,0x8614C70089AADE50E5A14DE1FB8FCF0880046E9494EEAD3BF600EBE451E335B4C9E21DE984912BCA15914711A9C359056A2AD0543035E971A2FAA387EA53AAD48A7016735E2BB60716626CAD6CF4F9CC41A59CF31EF07473A1DE08A018CAB7C6B95BF7AC9F501BD42FCC4C7CD834B6A7723B6ABCC9A98146A750A9222CCE2CC7L,0x8178408D7E1155B9F5B0665A3EDFE279189567AAC333CA33A7304AE1BB9C9A921735888FB7BC9B41550817B1C0D42B2AB0304546709648F45147180AD5FC839FB8F90B2D30772718A7B45E6204CE7886122874759F93C198CE61D10555F03C13FD83E639A637D849C846D5589029533E567E12FD992D690EC5EF38569327FC8DL
]
Nd = [
 #90252653600964453524559669296618135272911289775949194922543520872164147768650421038176330053599968601135821750672685664360786595430028684419411893316074286312793730822963564220564616708573764764386830123818197183233443472506106828919670406785228124876225200632055727680225997407097843708009916059133498338129L,
 146839643970016464813197409569004275595828791825722617066607993001682901023784267554815946189374651530288894322286859792246413142980277245909181062525398546369553995023529451396820549308690493928593324007689135648753323161394735120908960458860801743476353228970081369439513197105039143930008573928693059198131L,
 #94390533992358895550704225180484604016029781604622607833044135524814562613596803297695605669157378162035217814540004231075201420796787547733762265959320018107419058832819010681344133011777479722382525797938558181629835768471461434560813554411133962651212455645589624432040989600687436833459731886703583047283L,
 #111178307033150739104608647474199786251516913698936331430121060587893564405482896814045419370401816305592149685291034839621072343496556225594365571727260237484885924615887468053644519779081871778996851601207571981072261232384577126377714005550318990486619636734701266032569413421915520143377137845245405768733L,
 94154993593274109828418786834159728190797445711539243887409583756844882924221269576486611543668906670821879426307992404721925623741478677756083992902711765865503466687919799394258306574702184666207180530598057989884729154273423032471322027993848437082723045300784582836897839491321003685598931080456249945287L]
def BFFactor(fname,n):#细分
    s = time.clock()
    for f16bit in xrange(1, 65537):
        print '\r',f16bit,
        Xn = bin(f16bit)[2:].zfill(16)
        while len(Xn)<1000:
            Xn += bin((365 * int(Xn[-16:],2) - 1) % 2**16)[2:].zfill(16)
        while len(Xn)>980 and int(Xn,2):
            #print Xn
            if gcd(int(Xn,2),n)!=1:
                print '[+]Frame %s Factor found!' %fname
                print '  [-]Factor1:', int(Xn,2)
                print '  [-]Factor2:', n/int(Xn,2)
                print '[!]Timer:', round(time.clock()-s), 's'
                return ''
            Xn = Xn[:-1]
    return '[!!!]Factor not found!\n'
def FindFactors(fname,n):#小于 512bits
    s = time.clock()
    for f16bit in xrange(1, 65537):
        print '\r',f16bit,
        Xn = [f16bit]
        while len(Xn)<520:
            bin((365 * Xn[-1] - 1) % 2**16)[2:]
            xn = ''.join([bin(i)[2:] for i in Xn])
            if gcd(int(xn,2),n)!=1:
                print '[+]Frame %s Factor found!' %fname
                print '  [-]Factor1:', int(xn,2)
                print '  [-]Factor2:', n/int(xn,2)
                print '[!]Timer:', round(time.clock()-s), 's'
                return ''
    return '[!!!]Factor not found!\n'
s = time.clock()
for fname,n in enumerate(N):
    print FindFactors(fname,n)
print '[!]All Timer:', round(time.clock()-s), 's'