from AbstractTestClass import AbstractTestClass
from YandexAfishaCinemaParser import YandexAfishaCinemaParser
from Event import Event
from User import User
from Rating import Rating
from ParsingPointer import ParsingPointer


class TestYandexAfishaCinemaParser(AbstractTestClass):

    def test_parsing_page_with_one_event_in_full_mode(self, session, clear_data):
        event = Event({"source": "YandexAfishaCinema",
                       "title": "Веном",
                       "description": "С участием Вуди Харрельсона",
                       "id_kudago": "",
                       "categories_kudago": "",
                       "tags_kudago": [],
                       "price_kudago": "",
                       "url": "https://afisha.yandex.ru/moscow/cinema/venom-2018",
                       "categories": ["thriller", "adventure", "fiction", "action", "horror", "cinema"],
                       "image": "https://afisha.yandex.ru/13Iaf1251/27c773Ogd871/cJ/yU/brfj/bZMo/6yY-B/sPY9QJQ/1j/P7lMRq/TSKwKvH/0Lj2Ek/wemB6/u91a_Ez/em_Z/IF9R1/vDdq3k/2Xi4Bv/_GVHPvo/UU/oJY6/zxgm/zDFon-9/PC/2OWnZUN/yL/wUR26l/DMG_/Vxcv_/dBJWV5/VYfNP/Jo4rf64/ImPiGrp/0euRA/qNa/sft8dNl/DGZ1m-/Oe/56J/Mwci/JU/J3Vor7/WcVJ/HEjszJH/tORgJ/4EOJsD/_WQdkRG/W0/3DCoF6/fRrSJD/5yeId0/XNQZ_/Gjmz/FJSJ/y5m/9hpDHZ/cCT/nFaa/HGNt_/LP/dsJy1/GHpYVW/pv/fUwagB/ijqyk/M5UUp/4s_s/hig6n/za0K/S9Q3j/HVD/11i/Ix7V/M8isC/Re/9Q/W5Ym-n/0Y6D/q4/hAvUW/QXL/QQoFSzG/OL/Xq37lAE/hBg3/9dRrL0/dUQ/Jfg/Bao/uvdG/FJ/Er/dGZdBZd/tmot/q0fNga/CkHo/U3-e/AcNBOe/Urja81/9UQW8/U4xE0g-/mztske5/dArA/YPu7/8YiFnS/WWq8h/OHLob7h/Q5B5S/WFcXDUW/5nFgnnc/PQFR/01/ZdtivHX/zvoFr/av/Kv9_N8/dzMTF/_OYkl/SYDsVxS/ZBQP/J30/07R3JEm/d4yu/BOkzYwx/fO/syt/05r/-2mE0/KR/hxTg/YU/f1yX/owE2H/oU_Tia/oBv/qZj/77WRIy/fT6MCmy/010Ej/uSAV/y-5TAF/xV/YL/_8M/IY/ug/MCmH/lTRDbV/6evd/CoM63T/_4a/Nlj/XTkK/oLON/OJeYCr6/cl1Hk/q52/cBMm/g0l/iNmgMV/zNL/AyNe/_7/YyV/RS3-s4/iaA/JIXm/gCpCyD/eIdkD/SX/53MpE/POPwZ/u3WtJ/oS_vbCb/UGYuPI/9dmBtF/qKR/Vo/NIAMa6/rW/fA-eGS/3y9/WI5Z0h/ylc4vg/hG_ypoU/ZfMR/sVJQz/VmB755h/8i/IeeOpv/a5AC/wnI2zgS/xiwT/uQg/nweD4G/TRW/MEUuzx3/QyjSEj8/9lzNkBU/fIvtN/IcyqcK/NCF/z2/DJFOUO5/DtvSIXM/QKJW/XbTUqH/Ee5nG/eo/WsZ/s49Ec0w/EcSB0w/2hyRE/hvR/XH/bMhKMj/5egVUZ/3O/43R2qJJ/_Noy/F51g6/pe17x/eZ7V/hEjQA/jl4y/XV2s/DnIazL/aFJW/lF/NRKF9/JCHDN2/EIw/LTaXs/QQOI/OSn/s-X/cPWX/RBrf/MTgSWy/_oEKfNs/Tp3JY0/Gu/n7bJ/GxQ/IDbtFc/eI/8dxm0n3/yuFqBrF/YBbzW/w4oQhm/FDUa4/ykkBhSI/Kx/dxjC/1pZV/annBoo/Wj8/KvLn3/mBbhG/af/FFgO/-ofd4/VHU/HHaV/-8I9xRN/vU/qlbgs/2EQj70c/3Gm/gXhwZls/8xQBrw/sP/uvq/eBljQHy/I-/wG-FZHy/vyZI/xyeT/SmH/EfLP/xjW/bZGy/Vh/0mta/qSrte/QXI/AJCE/Jv16FOl/rNwFjK/4I6Y/5j3/dA6NMi/PR91o/renVev/dg_nT2u/ypQ/ES9UG/nlN57/VC4yrd/j2y/Qi/X_RM/VIcE/62EY/wg/CprAn6S/xrsW/wAwXiyZ/KliT/4E/onuiY/V7MpU/IU/ZHWr_/vGpklv/f2tLEjH/N7V/5XtJnh-/qHX/8ge/Bmb0Sl/er/ANl/KL8M/ylpsg9W/oe-V/4LJEE8/mBBGk/9VBH/4gHC_/T3TB/Nb/cnG7xj/Sn/Np76j/SJMwDK8/aW7tQp/PbrX36C/Bla/3WJ/6sQLNW/jP/hFZeu/O_hyJ/ed7E/QVq/GbMOe/5D1/VDGQATn/1y0/cnS/G1BhsQN/lz/qsz68dR/vgV/r2F/J2X/mZ_IJcx/QYYR/e9-eq/Mz_Fou/2TG/0j/z3/8XSboZy/Eb/ah-/EIG/eWxW8rk/g0_/1dJzCGV/2c7TdG/oczp/eu/NAWvrB/aR/KX-Rg/tdKz/Y_Y/lEnD8/SUOOC/9J6A/P83jK8/Z3WQ/Py2oKG/3USpTZ/4ks1/GBLAk/PdDuaz/B-dXmS_/ju8H/qX/6iw545z/WIVW7/sfJj5/hFvaODF/r2/GZ/dq/Drje/zXiG/aa/2A_t5H/dJ/CFyF/_D6Q/BcK7iU/AqT/EQHj1n/UQY/m1kn_A/ErzOR/x4/sNQeg/RmmB8/6X2_8K/B6zBQ/AT-/tXU/IUD2UM/Nyhyz/sg/fXWAj/Efh/QpfjCj/BXGC8l/ESvjoA-/vF/CK/lx2RJLS/MI0/Ni/8m5KG/3YG5pz/Uc9Bp/NOhfOQ/KA0/7PU/VGTBdti/OtkAq/60C3lk/HxVMH/OU/MxtR/ZfsPxm/EZ8i/Guv2Rzt/DZ1mb5S/edO/rz4nx/dcywa/fZ/WXKX6/fGoW3y/HTV/f6k/FqvB_/QWQLpEb/SCC-hq/COVbKA/ZjN/bYnWa3/-YiC5A/STj2mM/KZG/tgmc/YbrB/ybyoUwV/Pc3r/nFB5G/a-9/r5E6/iUU/W9Fh/cr8e5/38H1z-/TpwP0ag/PlR/QcOZ/DS/1AEyS/63c8pw/EZ-v/xTLEB/vWZnT/B7/YM/h--/eCF7/WNa1pf/sVui/MuDZs4/_I1/zdSleLL/9Jg/Bv0Dl/6c1/yEkGw/mUd/JWYg/jBp/Div/dSAJg/hBu/XrYyd/YTE/a42/QCNG/prd/oiJ82zC/vTmz/qQabc/v27/6ARRO9/HxLsj/PlTh/vsC4/agL8x/9A/ehAEQp/QI/pEBSaX1/bgicPh/zn/5kEIQnZ/hs/OAFohml/wr4D/R-sonn/Nx_0K/G8px7-/gMy/Yv5Hcp/Y6zXkBz/xC_/sif/lUQH/naAoLR/gOZF/0eR/1E4/0pS/Ao6/Ntr/DnZV/ZqTFIa/MAucWAH/XvEE/rJR/QOdZi/9Gsc/MU/YG/mXZTXuo/Jc9lMv/ULpIkr/5GI75/mA/jC2wLt/SB5ps/51NpMl/OtPqYT/VbUW/y1/zjq-J6/HxowlZ/wQi7YG/_rYJ/HY/gEb/PP/CVh/7nd8ngf/5eg7O/BLWUC-/FBItRw/FAh/gH/qQoWqPW/SzOC/HA3D9m/IQfnt7k/94Rrz2V",
                       "start_time": 4695148800,
                       "finish_time": 4695235199,
                       "join_anytime": True,
                       "duplicate_source_id": '',
                       "duplicate_id": 0,
                       "price_min": None,
                       "price_max": None
                       })
        parser = YandexAfishaCinemaParser(session)
        assert parser.main(mode="full", test_url="http://127.0.0.1:5000?source=yandexAfishaCinema&testcase=one_event_in_full_mode") == 2
        event_from_db = session.query(Event).first()
        self.check_equivalence_of_two_events(event, event_from_db)

    """
    def test_parsing_four_pages_in_full_mode(self, session, clear_data):
    """
    """
        This test case is about full mode
        The first page has only one event
        The second page has the same only one event
        The third page has two events - the same one and the new one
        The fourth page is 404
        Totally we have 2 events and 4 pages for parsing
        :param session:
        :param clear_data:
        :return:
        """
    """
        parsing_pointer = ParsingPointer.get_parsing_pointer(source="KudaGo", session=session)
        parsing_pointer.current_pointer = "1539356260"
        session.add(parsing_pointer)
        session.commit()
        parser = KudaGoParser(session)
        assert parser.main(mode='full', test_url="http://127.0.0.1:5000?source=kudago&testcase=four_pages_in_full_mode") == 4
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 2

    def test_parsing_page_with_bad_json_format_in_full_mode(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser.main(mode='full',
                           test_url="http://127.0.0.1:5000?source=kudago&testcase=page_with_bad_json_format") == 1
        events_from_db = session.query(Event).all()
        assert len(events_from_db) == 0

    def test_parsing_page_with_404_status_code(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser.main(test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == 1
        events_from_db = session.query(Event).all()
        assert [] == events_from_db

    def test_make_url_for_first_page(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser._make_url(page=1,
                                test_url=None) == "https://kudago.com/public-api/v1.4/events/?lang=ru&page_size=100&order_by=-publication_date&text_format=html&location=msk&is_free=0&fields=id,publication_date,dates,title,short_title,slug,place,description,body_text,location,categories,tagline,age_restriction,price,is_free,images,favorites_count,comments_count,site_url,tags,participants&page=1"

    def test_make_url_with_test_url(self, session, clear_data):
        parser = KudaGoParser(session)
        assert parser._make_url(page=1, test_url="http://127.0.0.1:5000?source=kudago&testcase=404") == "http://127.0.0.1:5000?source=kudago&testcase=404&page=1"
    """
