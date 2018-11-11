status = 200
mimetype = 'application/json; charset=utf-8'
resp = """
{
  "data": [
    {
      "event": {
        "id": "5a40246fcff2b3e888387d01",
        "url": "/moscow/theatre_show/beshenye-dengi-teatr-im-maiakovskogo",
        "title": "Бешеные деньги",
        "originalTitle": null,
        "dateReleased": null,
        "permanent": false,
        "systemTags": [
          {
            "code": "theatre"
          },
          {
            "code": "theatre_show"
          },
          {
            "code": "nearest-events"
          },
          {
            "code": "comedy"
          },
          {
            "code": "season-premiere"
          },
          {
            "code": "top-persons"
          },
          {
            "code": "hitprodazh-badge"
          },
          {
            "code": "newyear-vacations"
          },
          {
            "code": "theatre-feedback"
          },
          {
            "code": "family-theatre"
          },
          {
            "code": "traditional-theatre"
          }
        ],
        "argument": "В главной роли Светлана Немоляева",
        "promoArgument": null,
        "contentRating": "12+",
        "kinopoisk": null,
        "userRating": {
          "overall": {
            "value": 9.1,
            "count": 166
          }
        },
        "isFavorite": false,
        "type": {
          "id": "566991d27c650906c42d02b8",
          "code": "theatre",
          "type": "format",
          "status": "reviewed",
          "name": "Театр",
          "plural": {
            "one": "Театр",
            "some": "спектакля",
            "many": "спектаклей",
            "none": null
          },
          "nameCases": {
            "acc": "в театр",
            "gen": "театра"
          }
        },
        "tags": [
          {
            "id": "56bca4bf8323014e3902a6e8",
            "code": "theatre_show",
            "type": "format",
            "status": "approved",
            "name": "Спектакль",
            "plural": null,
            "nameCases": {
              "acc": "на спектакль",
              "gen": "спектакля"
            }
          },
          {
            "id": "57d28482377536932cfc4c2e",
            "code": "comedy",
            "type": "genre",
            "status": "approved",
            "name": "Комедия",
            "plural": null,
            "nameCases": {
              "acc": null,
              "gen": null
            }
          }
        ],
        "image": {
          "subType": "other",
          "source": {
            "id": "kudago",
            "title": "kudago.com",
            "url": "https://kudago.com/msk/event/teatr-beshenye-dengi/"
          },
          "bgColor": "#75446d",
          "eventCover": {
            "url": "https://avatars.mds.yandex.net/get-afishanew/21422/5543036bb12f14c5b8ac13e180071c83/s270x135",
            "width": 270,
            "height": 135,
            "precision": 1
          },
          "eventCoverXS": {
            "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnjMfcp39-qGNL1nqw-_hUG-iUbaXKNlQ7TOHXGC7Twh8qBagvJYCkHMF_fFPdskF0MUzLzg12Nx48mszbWPQAoMCH49IFdpkPUe4gsKn5SwHivl6i8jhDFmzL1xQT2dAGGjenCxS6hzT9SXpw0ZFffgVw1eMfXCYqPqPSxVvrJpDxktTCJUqfHXvXGYe3-l0C2JhVsdEQfg5z6_8WLujwMxQfuQcbq5Av-FBZa-uCVGwzb-3-NkIWIjW-9sBQ1BKG1I306Sl_pT5__yeejMxLPdCFeaTtPnwrVfzAKzrUySwXDIkRKYOUMcJIenH_m3pvDFry2BZkIx4WnOLKQtI4gPSh1dgOcqMyUdMppafMXiLFtmCU6C9cNlbV6Cgi1fEiMD2OJR6bhRr8SHVzzJxhdTBBwfEIQhocLJLGwWTpD4Pfr9boKFWbOGT1FJmB-HAo86lbntEubB5e5toHDvfyLQEikzAYurgw_UBQd92bV183RMnoKUMLETGh4fF85TCP3bHWxDtHvgRq4Qi6iuR-CfeZbb_MIUobWf3JHSro9AYXAZMwLaewA9x2R3bCuVxgGk3s2zplBD47nuzTa-4Duv2R5v8kQqwmRf44vrb3ZwTgsmqh8RpZDE7-6iss9skgBCC7CTSpsh3tQXJD4Zt-aQZQx-oERBwqIJDi33_HMqLtkdTgImG7J2ngCreJ_lYB2KVJnPM2Qh9w4MY8EuvqGTAZoRYaiqUF2mlVQcGhfl0BWefHHVMwPAqd789k0yeQ5ofA8ChkogJB3Sq6nPhzIN2dSq7VLFsfZcHCOxDf7yY1KK8qOaOUBex2U2fZpHBZDkv08jllFQ4JlNbJWskTufif7OIXY6QVSeI-pZ7PZzTbpGKO9hBwNlf1-Cg209MfIyqsNguIhBXtaHR1z4d3fzRD4tsVQAUIDb7rzE_UI7_jhuvwJ1yAImDcOJyn0Gkr_Z1CgvQVew9x3_4SLMrUFxEduSEQoooy8VZJQuKXWUwoaOftB0Y8LxW7_sJpzjuA0bPU4AlLnThHwwO5qc9vI9O_c7fVHn4vXuLjBTHG2CUnCYEqNKGTIeRMZG_wmkRpK37j2DtZKAIrsc7DS8Eist-e1usqU5olbuwGlK7eSxT1hXyq6CtKK1jc7yM23-8HMwGMJSmLgDzsc3xD5LNaRSpo1fIXWRcaDJDm7HnEN6P2mffAPm2dAGL9Fqih8lkryaFNsMojfy1y_NgFLczDMR0YsBUSgI8S_1N5ccK9Y1kIXsjTPlw3ITi4981G6w6E967LxwtUtDpl4CumlN52Hd-TXaPjEnkAffvBEyLz0hQGDJE1D4WwM9BhbFf4g2VfIU3E2QV3Hh8MmvD4fe8koeOE1ug7V6YBfsYUtInWcyDylW-e5DBgLUnU5yYE6c8MID-TAwuVjzvUVVFZ25JDYi9O4-k8ahgeAZvX41_LELz0tf3gJmmeNm32KZe1y1sM_rdLqvcXUz1rxuc9Kfb1PSE4sC4QhpIez25nWPmBR08OT_XfA34wFwGzw9lMyympx4f0xClOhR5-2w-hgsRJI_afV4PXC3gJTNT7ECfSxjQDJbsFEayCP9BcTGzct2R9CU7g7yt3OiE_teDZTOwIieOA6PwbYp8eUfwrpLbWeh3btFSQyS59MlHM7hIn2-YtFQK3Fx-ZrhL_V3FozodddDJN8dkFdhE0GL3x3nL-NaHzuNDDBnCvEU7zK6Oi93Aow6tfiNcMTBlT3sAUMPjxHx4fihQ9n5QOz29YT--Sf18RS-HHGHcQFx2f8-1q9AC534Ds-wJHlhRn4iW_t_VrAd6AQ43ICXgXVsDrFgHV5yQnLpYVBaqiFNttf1D_pERaGGfUziBDHQwIjsvuauUUhOW6z_ACU6E7Ut4npZH0aC3BmV6c7jl_Amjc4jca2NU3ASGKGR2tjDXgS3JxwK1bZhdN7s4rQT83KpHSzW7zFIbCocL_P2-8OFzsCLiQ0lkJ2oR3lPQ8XSFM_MsUKMTyJD4gig4VqZE67VxESceWUnw5aeHmCFwZIgO0z91_1TWqwpTc3Th2mDxY4C-Hr_lWF9q5WYfFMV4cbfTBNTvR0iYjHocpMpqgJNlfT1rarVhGB2bz8jZVNR87he_-e-oyg8Gb48kcSbYcUO46s4HoRz70p1S8ySF5OVrM7BU69esRIgK7Njm4iz7HWkhm-J5nYxNI9cEkWBkqOLjQzknsDr7_utf2BmuNEk3QH6WJ5HY53oFIvPcWTRF_weEDNPrLIxQfuy4ln6MRxnRHUvCGeHgle8vmOkUwFSOc1MlE7QSk_JLF9hVjmh5m1wewrORKH8GUT43BCkwgU8nEBQ3U8TIWCKkLEoGWPPNddkP8oG9hNVjszSNkATIate_JftQwo_Gh6eABQos7UuAAk5__SBTpnHyQ7ypRO23G2Bsl_cQ8GAqZCzeAtD3sS2RM77d6XxFGyOo_fiAvFaXB8VDTGLHguMjzDFOXEE3FFIis9Gob5pxwh9EUeQ5v0A",
            "width": 90,
            "height": 60,
            "precision": 1
          },
          "eventCoverS": {
            "url": "https://afisha.yandex.ru/267GrD643/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnhMeU6Xk1tTEc1yzlp6B6JcSof5HhM1c2f_3hKwrz7Tc4FYsrM5auE_9te2H6gXFaGXvD5SpSFD4cs-vgePYTqd2C1NYMT70AcM0Uv6fyezreolWi5gtZIVLdyysGzuclISW5JBenlDDXUU1n2Y1SRBNP__sHQD4vKLHS_mb1DI_ts8HhHG-BBmLnLYaQ7Hgs3ZhzqfUocRxKwusDBPPWBRQrkTobqIUnzFRURMK3QU8BeeDDGmkgHyC6z9pj_jO7-5bewTdjtDxB4wW4iddOOuKQboXgFF8eb-T8PDnn6jwLKIIKDZqtI9JuTGfYo1hhAkbV3DxJBiocme3Oaew1kf228uAGRLk6Tc0ptrL8Ti_9hV2c0BFOPnLn1RQ6_-sEBQ-zDTmttTL5UExo2pBfehh6zu8VVyATHqPj6mLKDqb-nfzjNmKeAkf4D4uO2noB97NCp9ooTw5a7-YmFdPJBwo-rBAsq5QP01FETd6BWEwyfcvnDHYhAhO-0M1S0gKZ8p_i4xpxjCd79huXrdFmD9a3cpH7NUAoX-j9NQ_31gEhKI8QLJ6JB-BwclrfnnpHDVDCwj9lBw08tO_AcMUJqse_wtMhbok1WdkEp6ntdRbboFmW5Qh7O0j__hY58cg8BzuuOBWHhwX-QUVv6r1YZQRM3-kOWyYVKK_hznzRIJvfr8LhPmiqIlj1GpWg0nwn3phOtdgKVyBbweA6Ls_VHz4PlyIKqaQS5nZtSOidYmUwS9bJI0IxOT6F7MNsyjSO7aTU9S5irzt93Se1rcd6Av-ddrbqLE05W9TBPinN4RoBCqYsNoqNI-ZAck7OhWdrNETE2hZmBxwMhuX6avQuusS6zNk8Xag9atUYobLFTRbrm0-eyg9xEnLm9QQ66-0mOBykLyq4pjP2QWxp3JNEbBJ-zMw_SiIMCoLPx2_hM4rCodXeLm2XGV38JqeL_FIY9L12vsYNdBlLwN8CAPH0ITAukzo9o4w90V1SVOu-VEIhYufJCVgkNS2aytJhxymS_ZPg4T5DgARH2zmcrvJNHvyTVI_zLH8ca-_iHxfs-C0CGIcCNoePJMJISHnGrFlfBGHxzTxkOyEApMDiYOUmi8-dzeM1YJgDWvIWmYP1XDrLtW6A7hFKKG_p3BMx6-EaIAyPDzmapTffQHdh6rhwQShg5_sWSDseGIPhyk_XI57etMrCHnSmBH_-B4m_-nAo9IlKsfQzQh1pw_wkF_DyNhYiljMJoa448VNXZNiefng0QtHmN2E-PiO3ydtu6Ayn-bX9_hlBny1F-Rq0sc9cB8KfeKHnGnMbRMz7PQH_zSczOYISKbyrB9B8ZXH-pEB-MmvC6j1aFRcdg-vcW9MIjdyh1-M2cZw_fuI8i6PSVAL_sn6T2h1RAmn41Bs02dc6Kx-xEB-4uzjYeFFM8IdRWA9lwc0NYwgRHI7q-0DxLLnBtubIPmyiB0nxDLaA7kkq075ct-4OdjF52sYbL_TIABoetjMyo6gl_WNqevGlQlwiRMDbO1wcORWOwu964iyA1IXUwRpjhRxh4iGQttlGOPy2dKvHLmoaTf3UBwL67DMTPKs4GaKCNdx8WFHFgHR_EEPBzgt0FTMjsMTMeuILofSh090iUakGYc0GtLPtVAvCm1-o1DBPH3bgzBIA-uUTCiqMNAustxnxU1NswZJERhl4wt89WhQYNpfM3X3cGZzcsevlHUy7Nm7SCbS0-XUB94NAo8wubS5d4t48Bu3GBDghkQkIjrEj7WNrReazUWQyW8TPI0cVGRWS7t9OxBOpxJ3T2SVIjA9r-xi6qOx3Gt6ea7_JMWgaU-fAFwTc6xIDGKAVCbaEFfd3aWL5o2dfN1Lo-ip_IRQOh__nTcQCvfmn6fouSJg4RM4kuLLKdhnygXKi2BdYHUbZ3B4lx-YgED6vCQWugzvWTE9v2JxuQAtdwsAqdCM2NaXg_m7AFL37gPL3IXWkJUfAFpevy1Ao1ppvi9ANXT9l_fw3BvX6BwMBrgkSpocm2UFYWeCbVUkRc-bPAlc-ECCMxeN-0TKc14DH6QNyvQFDxBqwkPR7J8iaUqXDPFA8WNz0PSfm7ycBHJAENYG0F8d1W1Lzhm5DK03p3RZpNzwdtPTDXdUNm_6DyNYXVoIvY8wUpaTaajbhtEyo-DBAG33rzBAH58seNh2MOCqKljzda15Vz6RdfA5Zx9slezoQKLfJ_G3nC6fDveniKEygFG3RKoCy0mYH5p5qtPgOdy9VzsEdEenEPgQrkTgylrEU8mpwWvusRWMVb_TlAmUnORes7fhq6gqt2b7B8ChfqANh-i2Yp_dmO8CBf7PJOGsuZOLJOBfQ6gQVKYYqF6GvId9fWWvqoGN0DH_Xwil8BggwlcTDatAzmd6z8tw-S4kSRM4an4TEfTnLqXeA1BZLM3_cxiQJ-MMxGyeEGheErgPeQE955bN0YTJbyeYOYBwpLZrU7VL-NLHMouv9LUaYDm_RP4uf93YbxKZ3jMModRtK3tA",
            "width": 100,
            "height": 60,
            "precision": 1
          },
          "eventCoverL": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsScoTc3-2dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
            "width": 380,
            "height": 250,
            "precision": 1
          },
          "eventCoverM": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsWTqDc092dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
            "width": 279,
            "height": 190,
            "precision": 1
          },
          "featured": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsSdoTc0-2dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
            "width": 390,
            "height": 150,
            "precision": 1
          },
          "featuredSelection": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsOWoTc0-mdT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
            "width": 420,
            "height": 140,
            "precision": 1
          },
          "headingPrimaryS": {
            "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsaWp399-mcYzyjlpf8rD4yUUZP7Pk0bdMDDMhPS2hwfAKEKBKeqGexWWErdk1d-NE3y8j5WPB47kMLOTcoKmMWFxfk6dYkUYscZib_HcQ_elU6J8RR-HEzO1B8z-NoQIgqzEzSVpT3dbHti4aVRXThu7PgKaiIzKbrT-k_zFIbGmuPJC2C-BEL7H5uV_kg4wJZYissydQ9v5ukHLNjyEh87kyY6vbsx0n1seeS8ckYCfefqPHUaLgCk4_JE7jCDzaXX3y5_ni9OziW4kdZ2IfugTrXDL1kaU8jrIgrPzS8LB6o5Oa6LJ-BVaGfepFFcFmTJ6QNABQgggtbOZ8wkid-j_dkOU78eacMjtL_6eBrQoFuq1hxAKlbZyz8J5uUsEwaSNx6fjBPXTXlM4KReXiVj0vM_WzYhPqTvzF3CAIL5mMraJV28Lk_kG76K3EUm9pR1oOADeyBv2PsXAdXXAz8kkTgvgJEG0WxEZuGse1o0ZOTZOF4-OB-l_sFA8Sey4ZT11idDvAJc9j6ChMhZBf2Ie4HkM00BctfdEgbOxBkbO5cTOaORBuRxTFXAmmxbK0bv5hVXGwsMg_HuSs4qkPafxuMHY4w5Q_MsoKvXaQHBm2KM8xhKH0_szgURzecvHSWqNSqCuT_9f05L8a1Zbghkze8JSjA6MqLp-lHAJJzitvf7F2O-JkXQO6GHyVsI_pJTicsPaSJNwNUWL9PLOCM4iQweu6Mg01xZU8aFfmwoXs3bDkMQFyu1xex7zSmM-aLiyRx1qjZP1SKEr_R7BeuUdqjON2oQa9rMFjryzz8hDIwzG4qtHPB1aFPwmnhKMFvD3wFRAyIPg-DeeMQQise41uACbYYkcNIkk6fLbxrpo2K8yA5CMEjm5z8IxvUsBwCwCg2IrgDCXnhD8YRfWCZ4xPk7WRULI6bw2HzuLY_SpebmGXSBNkDtAKSO9Wkj0Lxso-43YjxK4-wGLuzzFh0ZtwI_v7sX2XR2ZO26Ym8LaOrKJ3IQPTGgyf9k6ziB9L_-2StBviZu-h2-qepSBt6jaqvAFVMJa-jpJgHR7gEAFbswCauDHP13b3f4oE9CGWX37yRkFAgNv93SWuEIgNaw5-slbLwtTeIao4DFVyvZsk6c5i9cFFbd3SIH7-InBwyMEh2jjhPgXXxq8J9Xbg1M6cMlciIiIb_iyn3AIK_ktfL6DGudBlncHYaM1EcX1p5co9oLbQ501egkLc_VARwfoCQzurIj21ZzROO_UlwrQtDfB0Q_Awi6wvFJ6DGO25rL3Q1coQFs5TS8i8l6GeOyc5XMOX0dXeTuCSLIzBcTILEBKK6TA8ZTTGXMjUd6EXzW2S5XMwkzkevPfco2u-Ce4fgZdrwuXOYmh5DvRQv-unao4T9PIFrG9yQW5-oiNTqsGQ6dkTXCQ3NtyLl6dDJt8OQgVBQ5CoztznDLEaDCutXlDkeXJkHYHrCD33gowqdehO0daxRJ4cQ0NPXqORglligPmrIY2VBuSNOCTHUQfvTJAVUCDzWYxcdw4wWa0brs8D11ngJO_wWYkPJeHvWoTKvlNXc9af3vABPn9hQWAaUhLYe5M9h6fmnMsGdBNUjX-wZUFz8dkc_xTuUmmtGdzdAZcoI6fNMfmL_VehvBun-VyB50LnfY6jsO_-MWFgiFODugtSHWT1JE47taRSd47vI9VwYJM5Dk5GntN53vj_D4CUq6BWHBL5eg2noc1Zt1oNABfzZp-tsQDO3NEAErkgowvYgi9EloWNODc2IGbczZHlEWFy6R5cdszzWu94XF4CVyhj1l9haSict0AMCZbonNKmMzdv_vHgnz5hIwBoQxCYyUI8x8XkLHgVR9Flv33Bd9Ix4Wpejced4NrfeU0d0fSKU2ZeIhvbz3dhrmmG2l0jN-IlDP6As37-8zKwu2Ii-DiC_Ue3Bj_KdZXClS6OAYVxkeHafK51vBFI7zgtHfOFOoOVjePL6yxVkH575cgckuVypKysooE8_GEBkXkTEQgog43H9tbPGwb2QuaeH6NnMWNj667PJy5Ame4qTw8zhmthtfxxi6tsl-ONiVU5_JE3k5e8fJFTLHzDEKArEzDbyFH_tMXHLFs2R3M1LrwAh8BCIAs8DPStUpveab99o7aYkPe_g2mr7Hawz2hEK25w10AnfX7jAF_-ERCyaIBAyguQDwbndo27ZjSxFh1OUcUgIREr7s-knoFo3UncvnBUi9MGHaDZSj-U4a_ohzsc0raAJJ4NoYIPLsBwUpqDY6vbkY7ElfR9qYbH8Zecv-KmE8NgyjxcVSzBKK2ZzB_QZgrzBy0hqYiP5WD9uIT5fSPm8zf_zbKQz6yQE8B5InOKqrPdtXamrvsV1uFV_c5zpCGx0VgvTia-UpiuOl9foLU4MmZvMLvbzJUSzok02c-jZcLlHcxjIy9dUfFC6nKTaomz3-Vkhr8KdPYQZIydkeXD86CZjV_2T1B7LNot3oGkqiNWviF5aj7EU325hvk_U2UDlv0A",
            "width": 1181,
            "height": 400,
            "precision": 0.94
          },
          "microdata": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLn2oXN9jRj-jRKgC_so9ZqN9SGWY7PNVkIUNfkPA786g06Jqw5M4qrItN4TnTugm9cBkTg6SlVFz4Vvff7WucJvcWw59s8UpYuctovvqLJcD3-tV62wSJ0KHrX6AEE7vM9CCmICAmpgx7lfm14zZxlaDpazfsDRCM8LKPp-EXBOYzQh_f7AFSEBEvjGKCh33MH2L5NlekfbDda_-o8Nc7GMyA3hAcYvpgb_F12Qt6Xd14lYtDSHXQrNzGH7PN69S-pz6fc9zVupwBj3QGbl8lMD8WSWKnHHUkRTcDXKAn32TAzB5I1MLqGIeR-bFbHuXRhEH328jtBFxQTk-bhfN8pieOG7dA4aKsuT9M6sJfcUxr2i2is1j1UEmTo1DAIz9cXAgCmAiirrR_kcW5lwKJuXQtO3-wdeBUuHbftx0foKqLthd32H1ChG2nuBpaj8lks6bBildcNfBpX2vscKszYJh0dswQJloce7FRqdMeURFoORsbNHGkYMy6Q3d9L1yag84Xx5Q11nRV98iWdv_x4KNmGQ4jYK3kdTMnhODXK8zA-HbMxFJ60P9pDa2vln3t3B2P13jpmNzkRnf_IQOQTgNO1yvoIZ786YsIhoazldT_ygV214zhuCk_q1z4r99UjHzWKKBqcqg7tdl5Ix71yaxpIxOAbfiMiH5Pz3GnVC5DTh9X8K3C-FnzwKJ6l1HAH5aJgt88jfTRRxsAANtTsFyYvlQY5i7I5xVFcaP29RmwTaOn5DFI1CBKe48d9wDmbxZPF9i5pmz5B0CWLo_FRAt2hUpHVOn0hcMLHAgLR0xIXIaklELqyD9pXenD4s0JjAXvc3Tp3Bwsbp-X5Z_QQhd2_18kpb4w2fsQ6iZTlRQTkiXKy6RFUE0T41CQO7eoEFSK1Fzuqog7EcGhm27RkWQlt9fEfZwEPMZrg7HrEFp7EuMX5Fku7H0DCA7CL61oi3al-sOwabTVu_u4-F-riNiI3ogwRpIUS-k1fS8uaV0UiaMPjGV4mFzSP7spg3Cms8YfV1wFWoThf-Sa-lO1SDP-YS5HnH00aU-P5Ixvm0AA2D6koEr2WB-BgclnGh3JGNGz23wZKCyk-v-_ob8UbotyF3vQZUbwRcPwLuYXJZSrFl1as0itJHG3v3yQC0fIUPgKmNTiuiw_feF5N75leRyJa3PMGdRMOH5fA2mrQCovbpPXgJ1aZHWHsN7ap21oW4aZMjtoeTzZN2Pk_Ef3EOic-lg4zoaUc_31sa-GgQmUUR_3aA1UoOjeG4eVF6S2K7Jjy1R5_oxp80TmDhfRsANO2X6frGGI5SsHvMC7s4SEzH7YTNp6EM81oSlHfpkRMB0v34Sh8Fg4VgdTeQcMInsaF3eUdbZgBWu4rno3xUS3VhGKgyQFPDWXn2hY08fkHAB2AFyahjDf5VURyzoB5QgRsx9g1ehcDFKbP_GX3FYn3rtX4I1WvEmrTCKKQ2X0h96BWs-4yXy9358E7K8vIBgc-rQw1vKkswmNFUN2EVGMFevHnIVIeAzyy9e9lzgC6xafx9wROhwFH9T6Vn8tSKd-8f5PyGWsIZfvsNQ_4wSQaNYYNH6yIM_BIcXXrp2ZkBG_BzyhYKD06kfXvQu8gnsK7ycUoVIcuYNE7oY34bAT0v2yN1xxQFX3u7jUG2NgyPTmUAyqApRz7dXVn255vXwd-9-Epcz0aMoDy0VDSCI76g_bYOmSIMW_RPLWs8lkc67R0k_UtexdvwOgiJc_qOSAElyEsurksw1xSRs68RHwBbun8KHIeHxCCwcla5xCiwr_O3A1djRh-3yCgrulwAcCocYzwGXUScevqEwjZ0QARGJYZGYyjOMF7TVb4h0F1LVvgxBx_BQoBusLJS_MtmPicxdwZaqItQt06hq_qXB7ZtWCqwB5gLG3iywgF68ImHgSaAR6iggPndmxp8Zh9egdh4M8eXT4oHqPhzV3zL7_jkcrhJXehI3DyJ4eJ23gFxJxosMU8QwhNy-g6GczRGR8EjQkav40O8EBUbsqRZ1QjbsjsA3srATu-8dx70gO_1o_o5jxTpSd81Ri4otRmBfmye4HIP34pRcHJKQzs0wQhCaouKY6TOvNLR3Pxm11qLHzc0gpXFjkKntLYRNUqvNmw_MIDfYUvcsAslrPFTyvnv0CN2BhbHn3s6Sgo1eQFPTW1JQuliST2THtRwqR4fgJ678AHeyM6N6Hi6kLpF4L4hMPYIUaLMkzlOp6_9EgBwaNAs-8scztw4f8mJ_XWMyA1rTksjaYl2ENPWdq7Y0gxRMjeGlIcIROl5edD4w2B0JbDyylRhxlL_S-7v8huHtSkcYXzLUIXeMT5HwnPxzE3J4gOMriLEPFyXlX8rHpYEmPjxztjOxg6nuXdetcKjOO61d8IQKItfPoMiKTKZTbcl2yr0zBZKXfY5zcg-sk_NReIKzOaig_nYFFG67lEfAxHxNshQiYXKrDd833_GJ36m8bSGVyJMlnuF7uv6Go53Jt7le0YbCth",
            "width": 1181,
            "height": 787,
            "precision": 1
          },
          "suggest": {
            "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsaXoTc8_ixOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
            "width": 130,
            "height": 90,
            "precision": 1
          },
          "type": "image",
          "sizes": {
            "eventCover": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/21422/5543036bb12f14c5b8ac13e180071c83/s270x135",
              "width": 270,
              "height": 135,
              "precision": 1
            },
            "eventCoverXS": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnjMfcp39-qGNL1nqw-_hUG-iUbaXKNlQ7TOHXGC7Twh8qBagvJYCkHMF_fFPdskF0MUzLzg12Nx48mszbWPQAoMCH49IFdpkPUe4gsKn5SwHivl6i8jhDFmzL1xQT2dAGGjenCxS6hzT9SXpw0ZFffgVw1eMfXCYqPqPSxVvrJpDxktTCJUqfHXvXGYe3-l0C2JhVsdEQfg5z6_8WLujwMxQfuQcbq5Av-FBZa-uCVGwzb-3-NkIWIjW-9sBQ1BKG1I306Sl_pT5__yeejMxLPdCFeaTtPnwrVfzAKzrUySwXDIkRKYOUMcJIenH_m3pvDFry2BZkIx4WnOLKQtI4gPSh1dgOcqMyUdMppafMXiLFtmCU6C9cNlbV6Cgi1fEiMD2OJR6bhRr8SHVzzJxhdTBBwfEIQhocLJLGwWTpD4Pfr9boKFWbOGT1FJmB-HAo86lbntEubB5e5toHDvfyLQEikzAYurgw_UBQd92bV183RMnoKUMLETGh4fF85TCP3bHWxDtHvgRq4Qi6iuR-CfeZbb_MIUobWf3JHSro9AYXAZMwLaewA9x2R3bCuVxgGk3s2zplBD47nuzTa-4Duv2R5v8kQqwmRf44vrb3ZwTgsmqh8RpZDE7-6iss9skgBCC7CTSpsh3tQXJD4Zt-aQZQx-oERBwqIJDi33_HMqLtkdTgImG7J2ngCreJ_lYB2KVJnPM2Qh9w4MY8EuvqGTAZoRYaiqUF2mlVQcGhfl0BWefHHVMwPAqd789k0yeQ5ofA8ChkogJB3Sq6nPhzIN2dSq7VLFsfZcHCOxDf7yY1KK8qOaOUBex2U2fZpHBZDkv08jllFQ4JlNbJWskTufif7OIXY6QVSeI-pZ7PZzTbpGKO9hBwNlf1-Cg209MfIyqsNguIhBXtaHR1z4d3fzRD4tsVQAUIDb7rzE_UI7_jhuvwJ1yAImDcOJyn0Gkr_Z1CgvQVew9x3_4SLMrUFxEduSEQoooy8VZJQuKXWUwoaOftB0Y8LxW7_sJpzjuA0bPU4AlLnThHwwO5qc9vI9O_c7fVHn4vXuLjBTHG2CUnCYEqNKGTIeRMZG_wmkRpK37j2DtZKAIrsc7DS8Eist-e1usqU5olbuwGlK7eSxT1hXyq6CtKK1jc7yM23-8HMwGMJSmLgDzsc3xD5LNaRSpo1fIXWRcaDJDm7HnEN6P2mffAPm2dAGL9Fqih8lkryaFNsMojfy1y_NgFLczDMR0YsBUSgI8S_1N5ccK9Y1kIXsjTPlw3ITi4981G6w6E967LxwtUtDpl4CumlN52Hd-TXaPjEnkAffvBEyLz0hQGDJE1D4WwM9BhbFf4g2VfIU3E2QV3Hh8MmvD4fe8koeOE1ug7V6YBfsYUtInWcyDylW-e5DBgLUnU5yYE6c8MID-TAwuVjzvUVVFZ25JDYi9O4-k8ahgeAZvX41_LELz0tf3gJmmeNm32KZe1y1sM_rdLqvcXUz1rxuc9Kfb1PSE4sC4QhpIez25nWPmBR08OT_XfA34wFwGzw9lMyympx4f0xClOhR5-2w-hgsRJI_afV4PXC3gJTNT7ECfSxjQDJbsFEayCP9BcTGzct2R9CU7g7yt3OiE_teDZTOwIieOA6PwbYp8eUfwrpLbWeh3btFSQyS59MlHM7hIn2-YtFQK3Fx-ZrhL_V3FozodddDJN8dkFdhE0GL3x3nL-NaHzuNDDBnCvEU7zK6Oi93Aow6tfiNcMTBlT3sAUMPjxHx4fihQ9n5QOz29YT--Sf18RS-HHGHcQFx2f8-1q9AC534Ds-wJHlhRn4iW_t_VrAd6AQ43ICXgXVsDrFgHV5yQnLpYVBaqiFNttf1D_pERaGGfUziBDHQwIjsvuauUUhOW6z_ACU6E7Ut4npZH0aC3BmV6c7jl_Amjc4jca2NU3ASGKGR2tjDXgS3JxwK1bZhdN7s4rQT83KpHSzW7zFIbCocL_P2-8OFzsCLiQ0lkJ2oR3lPQ8XSFM_MsUKMTyJD4gig4VqZE67VxESceWUnw5aeHmCFwZIgO0z91_1TWqwpTc3Th2mDxY4C-Hr_lWF9q5WYfFMV4cbfTBNTvR0iYjHocpMpqgJNlfT1rarVhGB2bz8jZVNR87he_-e-oyg8Gb48kcSbYcUO46s4HoRz70p1S8ySF5OVrM7BU69esRIgK7Njm4iz7HWkhm-J5nYxNI9cEkWBkqOLjQzknsDr7_utf2BmuNEk3QH6WJ5HY53oFIvPcWTRF_weEDNPrLIxQfuy4ln6MRxnRHUvCGeHgle8vmOkUwFSOc1MlE7QSk_JLF9hVjmh5m1wewrORKH8GUT43BCkwgU8nEBQ3U8TIWCKkLEoGWPPNddkP8oG9hNVjszSNkATIate_JftQwo_Gh6eABQos7UuAAk5__SBTpnHyQ7ypRO23G2Bsl_cQ8GAqZCzeAtD3sS2RM77d6XxFGyOo_fiAvFaXB8VDTGLHguMjzDFOXEE3FFIis9Gob5pxwh9EUeQ5v0A",
              "width": 90,
              "height": 60,
              "precision": 1
            },
            "eventCoverS": {
              "url": "https://afisha.yandex.ru/267GrD643/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnhMeU6Xk1tTEc1yzlp6B6JcSof5HhM1c2f_3hKwrz7Tc4FYsrM5auE_9te2H6gXFaGXvD5SpSFD4cs-vgePYTqd2C1NYMT70AcM0Uv6fyezreolWi5gtZIVLdyysGzuclISW5JBenlDDXUU1n2Y1SRBNP__sHQD4vKLHS_mb1DI_ts8HhHG-BBmLnLYaQ7Hgs3ZhzqfUocRxKwusDBPPWBRQrkTobqIUnzFRURMK3QU8BeeDDGmkgHyC6z9pj_jO7-5bewTdjtDxB4wW4iddOOuKQboXgFF8eb-T8PDnn6jwLKIIKDZqtI9JuTGfYo1hhAkbV3DxJBiocme3Oaew1kf228uAGRLk6Tc0ptrL8Ti_9hV2c0BFOPnLn1RQ6_-sEBQ-zDTmttTL5UExo2pBfehh6zu8VVyATHqPj6mLKDqb-nfzjNmKeAkf4D4uO2noB97NCp9ooTw5a7-YmFdPJBwo-rBAsq5QP01FETd6BWEwyfcvnDHYhAhO-0M1S0gKZ8p_i4xpxjCd79huXrdFmD9a3cpH7NUAoX-j9NQ_31gEhKI8QLJ6JB-BwclrfnnpHDVDCwj9lBw08tO_AcMUJqse_wtMhbok1WdkEp6ntdRbboFmW5Qh7O0j__hY58cg8BzuuOBWHhwX-QUVv6r1YZQRM3-kOWyYVKK_hznzRIJvfr8LhPmiqIlj1GpWg0nwn3phOtdgKVyBbweA6Ls_VHz4PlyIKqaQS5nZtSOidYmUwS9bJI0IxOT6F7MNsyjSO7aTU9S5irzt93Se1rcd6Av-ddrbqLE05W9TBPinN4RoBCqYsNoqNI-ZAck7OhWdrNETE2hZmBxwMhuX6avQuusS6zNk8Xag9atUYobLFTRbrm0-eyg9xEnLm9QQ66-0mOBykLyq4pjP2QWxp3JNEbBJ-zMw_SiIMCoLPx2_hM4rCodXeLm2XGV38JqeL_FIY9L12vsYNdBlLwN8CAPH0ITAukzo9o4w90V1SVOu-VEIhYufJCVgkNS2aytJhxymS_ZPg4T5DgARH2zmcrvJNHvyTVI_zLH8ca-_iHxfs-C0CGIcCNoePJMJISHnGrFlfBGHxzTxkOyEApMDiYOUmi8-dzeM1YJgDWvIWmYP1XDrLtW6A7hFKKG_p3BMx6-EaIAyPDzmapTffQHdh6rhwQShg5_sWSDseGIPhyk_XI57etMrCHnSmBH_-B4m_-nAo9IlKsfQzQh1pw_wkF_DyNhYiljMJoa448VNXZNiefng0QtHmN2E-PiO3ydtu6Ayn-bX9_hlBny1F-Rq0sc9cB8KfeKHnGnMbRMz7PQH_zSczOYISKbyrB9B8ZXH-pEB-MmvC6j1aFRcdg-vcW9MIjdyh1-M2cZw_fuI8i6PSVAL_sn6T2h1RAmn41Bs02dc6Kx-xEB-4uzjYeFFM8IdRWA9lwc0NYwgRHI7q-0DxLLnBtubIPmyiB0nxDLaA7kkq075ct-4OdjF52sYbL_TIABoetjMyo6gl_WNqevGlQlwiRMDbO1wcORWOwu964iyA1IXUwRpjhRxh4iGQttlGOPy2dKvHLmoaTf3UBwL67DMTPKs4GaKCNdx8WFHFgHR_EEPBzgt0FTMjsMTMeuILofSh090iUakGYc0GtLPtVAvCm1-o1DBPH3bgzBIA-uUTCiqMNAustxnxU1NswZJERhl4wt89WhQYNpfM3X3cGZzcsevlHUy7Nm7SCbS0-XUB94NAo8wubS5d4t48Bu3GBDghkQkIjrEj7WNrReazUWQyW8TPI0cVGRWS7t9OxBOpxJ3T2SVIjA9r-xi6qOx3Gt6ea7_JMWgaU-fAFwTc6xIDGKAVCbaEFfd3aWL5o2dfN1Lo-ip_IRQOh__nTcQCvfmn6fouSJg4RM4kuLLKdhnygXKi2BdYHUbZ3B4lx-YgED6vCQWugzvWTE9v2JxuQAtdwsAqdCM2NaXg_m7AFL37gPL3IXWkJUfAFpevy1Ao1ppvi9ANXT9l_fw3BvX6BwMBrgkSpocm2UFYWeCbVUkRc-bPAlc-ECCMxeN-0TKc14DH6QNyvQFDxBqwkPR7J8iaUqXDPFA8WNz0PSfm7ycBHJAENYG0F8d1W1Lzhm5DK03p3RZpNzwdtPTDXdUNm_6DyNYXVoIvY8wUpaTaajbhtEyo-DBAG33rzBAH58seNh2MOCqKljzda15Vz6RdfA5Zx9slezoQKLfJ_G3nC6fDveniKEygFG3RKoCy0mYH5p5qtPgOdy9VzsEdEenEPgQrkTgylrEU8mpwWvusRWMVb_TlAmUnORes7fhq6gqt2b7B8ChfqANh-i2Yp_dmO8CBf7PJOGsuZOLJOBfQ6gQVKYYqF6GvId9fWWvqoGN0DH_Xwil8BggwlcTDatAzmd6z8tw-S4kSRM4an4TEfTnLqXeA1BZLM3_cxiQJ-MMxGyeEGheErgPeQE955bN0YTJbyeYOYBwpLZrU7VL-NLHMouv9LUaYDm_RP4uf93YbxKZ3jMModRtK3tA",
              "width": 100,
              "height": 60,
              "precision": 1
            },
            "eventCoverL": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/21422/5543036bb12f14c5b8ac13e180071c83/s380x250",
              "width": 380,
              "height": 250,
              "precision": 1
            },
            "eventCoverM": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsWTqDc092dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
              "width": 279,
              "height": 190,
              "precision": 1
            },
            "featured": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/21422/5543036bb12f14c5b8ac13e180071c83/s390x150",
              "width": 390,
              "height": 150,
              "precision": 1
            },
            "featuredSelection": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsOWoTc0-mdT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
              "width": 420,
              "height": 140,
              "precision": 1
            },
            "headingPrimaryS": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsaWp399-mcYzyjlpf8rD4yUUZP7Pk0bdMDDMhPS2hwfAKEKBKeqGexWWErdk1d-NE3y8j5WPB47kMLOTcoKmMWFxfk6dYkUYscZib_HcQ_elU6J8RR-HEzO1B8z-NoQIgqzEzSVpT3dbHti4aVRXThu7PgKaiIzKbrT-k_zFIbGmuPJC2C-BEL7H5uV_kg4wJZYissydQ9v5ukHLNjyEh87kyY6vbsx0n1seeS8ckYCfefqPHUaLgCk4_JE7jCDzaXX3y5_ni9OziW4kdZ2IfugTrXDL1kaU8jrIgrPzS8LB6o5Oa6LJ-BVaGfepFFcFmTJ6QNABQgggtbOZ8wkid-j_dkOU78eacMjtL_6eBrQoFuq1hxAKlbZyz8J5uUsEwaSNx6fjBPXTXlM4KReXiVj0vM_WzYhPqTvzF3CAIL5mMraJV28Lk_kG76K3EUm9pR1oOADeyBv2PsXAdXXAz8kkTgvgJEG0WxEZuGse1o0ZOTZOF4-OB-l_sFA8Sey4ZT11idDvAJc9j6ChMhZBf2Ie4HkM00BctfdEgbOxBkbO5cTOaORBuRxTFXAmmxbK0bv5hVXGwsMg_HuSs4qkPafxuMHY4w5Q_MsoKvXaQHBm2KM8xhKH0_szgURzecvHSWqNSqCuT_9f05L8a1Zbghkze8JSjA6MqLp-lHAJJzitvf7F2O-JkXQO6GHyVsI_pJTicsPaSJNwNUWL9PLOCM4iQweu6Mg01xZU8aFfmwoXs3bDkMQFyu1xex7zSmM-aLiyRx1qjZP1SKEr_R7BeuUdqjON2oQa9rMFjryzz8hDIwzG4qtHPB1aFPwmnhKMFvD3wFRAyIPg-DeeMQQise41uACbYYkcNIkk6fLbxrpo2K8yA5CMEjm5z8IxvUsBwCwCg2IrgDCXnhD8YRfWCZ4xPk7WRULI6bw2HzuLY_SpebmGXSBNkDtAKSO9Wkj0Lxso-43YjxK4-wGLuzzFh0ZtwI_v7sX2XR2ZO26Ym8LaOrKJ3IQPTGgyf9k6ziB9L_-2StBviZu-h2-qepSBt6jaqvAFVMJa-jpJgHR7gEAFbswCauDHP13b3f4oE9CGWX37yRkFAgNv93SWuEIgNaw5-slbLwtTeIao4DFVyvZsk6c5i9cFFbd3SIH7-InBwyMEh2jjhPgXXxq8J9Xbg1M6cMlciIiIb_iyn3AIK_ktfL6DGudBlncHYaM1EcX1p5co9oLbQ501egkLc_VARwfoCQzurIj21ZzROO_UlwrQtDfB0Q_Awi6wvFJ6DGO25rL3Q1coQFs5TS8i8l6GeOyc5XMOX0dXeTuCSLIzBcTILEBKK6TA8ZTTGXMjUd6EXzW2S5XMwkzkevPfco2u-Ce4fgZdrwuXOYmh5DvRQv-unao4T9PIFrG9yQW5-oiNTqsGQ6dkTXCQ3NtyLl6dDJt8OQgVBQ5CoztznDLEaDCutXlDkeXJkHYHrCD33gowqdehO0daxRJ4cQ0NPXqORglligPmrIY2VBuSNOCTHUQfvTJAVUCDzWYxcdw4wWa0brs8D11ngJO_wWYkPJeHvWoTKvlNXc9af3vABPn9hQWAaUhLYe5M9h6fmnMsGdBNUjX-wZUFz8dkc_xTuUmmtGdzdAZcoI6fNMfmL_VehvBun-VyB50LnfY6jsO_-MWFgiFODugtSHWT1JE47taRSd47vI9VwYJM5Dk5GntN53vj_D4CUq6BWHBL5eg2noc1Zt1oNABfzZp-tsQDO3NEAErkgowvYgi9EloWNODc2IGbczZHlEWFy6R5cdszzWu94XF4CVyhj1l9haSict0AMCZbonNKmMzdv_vHgnz5hIwBoQxCYyUI8x8XkLHgVR9Flv33Bd9Ix4Wpejced4NrfeU0d0fSKU2ZeIhvbz3dhrmmG2l0jN-IlDP6As37-8zKwu2Ii-DiC_Ue3Bj_KdZXClS6OAYVxkeHafK51vBFI7zgtHfOFOoOVjePL6yxVkH575cgckuVypKysooE8_GEBkXkTEQgog43H9tbPGwb2QuaeH6NnMWNj667PJy5Ame4qTw8zhmthtfxxi6tsl-ONiVU5_JE3k5e8fJFTLHzDEKArEzDbyFH_tMXHLFs2R3M1LrwAh8BCIAs8DPStUpveab99o7aYkPe_g2mr7Hawz2hEK25w10AnfX7jAF_-ERCyaIBAyguQDwbndo27ZjSxFh1OUcUgIREr7s-knoFo3UncvnBUi9MGHaDZSj-U4a_ohzsc0raAJJ4NoYIPLsBwUpqDY6vbkY7ElfR9qYbH8Zecv-KmE8NgyjxcVSzBKK2ZzB_QZgrzBy0hqYiP5WD9uIT5fSPm8zf_zbKQz6yQE8B5InOKqrPdtXamrvsV1uFV_c5zpCGx0VgvTia-UpiuOl9foLU4MmZvMLvbzJUSzok02c-jZcLlHcxjIy9dUfFC6nKTaomz3-Vkhr8KdPYQZIydkeXD86CZjV_2T1B7LNot3oGkqiNWviF5aj7EU325hvk_U2UDlv0A",
              "width": 1181,
              "height": 400,
              "precision": 0.94
            },
            "microdata": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLn2oXN9jRj-jRKgC_so9ZqN9SGWY7PNVkIUNfkPA786g06Jqw5M4qrItN4TnTugm9cBkTg6SlVFz4Vvff7WucJvcWw59s8UpYuctovvqLJcD3-tV62wSJ0KHrX6AEE7vM9CCmICAmpgx7lfm14zZxlaDpazfsDRCM8LKPp-EXBOYzQh_f7AFSEBEvjGKCh33MH2L5NlekfbDda_-o8Nc7GMyA3hAcYvpgb_F12Qt6Xd14lYtDSHXQrNzGH7PN69S-pz6fc9zVupwBj3QGbl8lMD8WSWKnHHUkRTcDXKAn32TAzB5I1MLqGIeR-bFbHuXRhEH328jtBFxQTk-bhfN8pieOG7dA4aKsuT9M6sJfcUxr2i2is1j1UEmTo1DAIz9cXAgCmAiirrR_kcW5lwKJuXQtO3-wdeBUuHbftx0foKqLthd32H1ChG2nuBpaj8lks6bBildcNfBpX2vscKszYJh0dswQJloce7FRqdMeURFoORsbNHGkYMy6Q3d9L1yag84Xx5Q11nRV98iWdv_x4KNmGQ4jYK3kdTMnhODXK8zA-HbMxFJ60P9pDa2vln3t3B2P13jpmNzkRnf_IQOQTgNO1yvoIZ786YsIhoazldT_ygV214zhuCk_q1z4r99UjHzWKKBqcqg7tdl5Ix71yaxpIxOAbfiMiH5Pz3GnVC5DTh9X8K3C-FnzwKJ6l1HAH5aJgt88jfTRRxsAANtTsFyYvlQY5i7I5xVFcaP29RmwTaOn5DFI1CBKe48d9wDmbxZPF9i5pmz5B0CWLo_FRAt2hUpHVOn0hcMLHAgLR0xIXIaklELqyD9pXenD4s0JjAXvc3Tp3Bwsbp-X5Z_QQhd2_18kpb4w2fsQ6iZTlRQTkiXKy6RFUE0T41CQO7eoEFSK1Fzuqog7EcGhm27RkWQlt9fEfZwEPMZrg7HrEFp7EuMX5Fku7H0DCA7CL61oi3al-sOwabTVu_u4-F-riNiI3ogwRpIUS-k1fS8uaV0UiaMPjGV4mFzSP7spg3Cms8YfV1wFWoThf-Sa-lO1SDP-YS5HnH00aU-P5Ixvm0AA2D6koEr2WB-BgclnGh3JGNGz23wZKCyk-v-_ob8UbotyF3vQZUbwRcPwLuYXJZSrFl1as0itJHG3v3yQC0fIUPgKmNTiuiw_feF5N75leRyJa3PMGdRMOH5fA2mrQCovbpPXgJ1aZHWHsN7ap21oW4aZMjtoeTzZN2Pk_Ef3EOic-lg4zoaUc_31sa-GgQmUUR_3aA1UoOjeG4eVF6S2K7Jjy1R5_oxp80TmDhfRsANO2X6frGGI5SsHvMC7s4SEzH7YTNp6EM81oSlHfpkRMB0v34Sh8Fg4VgdTeQcMInsaF3eUdbZgBWu4rno3xUS3VhGKgyQFPDWXn2hY08fkHAB2AFyahjDf5VURyzoB5QgRsx9g1ehcDFKbP_GX3FYn3rtX4I1WvEmrTCKKQ2X0h96BWs-4yXy9358E7K8vIBgc-rQw1vKkswmNFUN2EVGMFevHnIVIeAzyy9e9lzgC6xafx9wROhwFH9T6Vn8tSKd-8f5PyGWsIZfvsNQ_4wSQaNYYNH6yIM_BIcXXrp2ZkBG_BzyhYKD06kfXvQu8gnsK7ycUoVIcuYNE7oY34bAT0v2yN1xxQFX3u7jUG2NgyPTmUAyqApRz7dXVn255vXwd-9-Epcz0aMoDy0VDSCI76g_bYOmSIMW_RPLWs8lkc67R0k_UtexdvwOgiJc_qOSAElyEsurksw1xSRs68RHwBbun8KHIeHxCCwcla5xCiwr_O3A1djRh-3yCgrulwAcCocYzwGXUScevqEwjZ0QARGJYZGYyjOMF7TVb4h0F1LVvgxBx_BQoBusLJS_MtmPicxdwZaqItQt06hq_qXB7ZtWCqwB5gLG3iywgF68ImHgSaAR6iggPndmxp8Zh9egdh4M8eXT4oHqPhzV3zL7_jkcrhJXehI3DyJ4eJ23gFxJxosMU8QwhNy-g6GczRGR8EjQkav40O8EBUbsqRZ1QjbsjsA3srATu-8dx70gO_1o_o5jxTpSd81Ri4otRmBfmye4HIP34pRcHJKQzs0wQhCaouKY6TOvNLR3Pxm11qLHzc0gpXFjkKntLYRNUqvNmw_MIDfYUvcsAslrPFTyvnv0CN2BhbHn3s6Sgo1eQFPTW1JQuliST2THtRwqR4fgJ678AHeyM6N6Hi6kLpF4L4hMPYIUaLMkzlOp6_9EgBwaNAs-8scztw4f8mJ_XWMyA1rTksjaYl2ENPWdq7Y0gxRMjeGlIcIROl5edD4w2B0JbDyylRhxlL_S-7v8huHtSkcYXzLUIXeMT5HwnPxzE3J4gOMriLEPFyXlX8rHpYEmPjxztjOxg6nuXdetcKjOO61d8IQKItfPoMiKTKZTbcl2yr0zBZKXfY5zcg-sk_NReIKzOaig_nYFFG67lEfAxHxNshQiYXKrDd833_GJ36m8bSGVyJMlnuF7uv6Go53Jt7le0YbCth",
              "width": 1181,
              "height": 787,
              "precision": 1
            },
            "suggest": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPYEd58HBv2aMUpAtbEb22I29YS8a6XFVjY2nmkLpLvlLnxsaXoTc8_ixOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
              "width": 130,
              "height": 90,
              "precision": 1
            }
          }
        },
        "tickets": [
          {
            "id": "55248",
            "price": {
              "currency": "rub",
              "min": 40000,
              "max": 600000
            },
            "discountPercents": []
          },
          {
            "id": "55248",
            "price": {
              "currency": "rub",
              "min": 40000,
              "max": 600000
            },
            "discountPercents": []
          }
        ]
      },
      "scheduleInfo": {
        "dates": [
          "2118-10-14"
        ],
        "dateStarted": "2017-04-07",
        "dateEnd": "2019-01-19",
        "dateReleased": null,
        "permanent": false,
        "onlyPlace": {
          "id": "560adaf2fc8131343bee2c29",
          "url": "/moscow/theatre/places/teatr-im-maiakovskogo",
          "title": "Театр им. Маяковского",
          "logo": {
            "bgColor": "#384e78",
            "microdata": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHn2oXN9jRj-jRKgC_so9ZqN9SGWY7PNVkIUNfkPA786g06Jqw5M4qrItN4TnTugm9cBkTg6SlVFz4Vvff7WucJvcWw59s8UpYuctovvqLJcD3-tV62wSJ0KHrX6AEE7vM9CCmICAmpgx7lfm14zZxlaDpazfsDRCM8LKPp-EXBOYzQh_f7AFSEBEvjGKCh33MH2L5NlekfbDda_-o8Nc7GMyA3hAcYvpgb_F12Qt6Xd14lYtDSHXQrNzGH7PN69S-pz6fc9zVupwBj3QGbl8lMD8WSWKnHHUkRTcDXKAn32TAzB5I1MLqGIeR-bFbHuXRhEH328jtBFxQTk-bhfN8pieOG7dA4aKsuT9M6sJfcUxr2i2is1j1UEmTo1DAIz9cXAgCmAiirrR_kcW5lwKJuXQtO3-wdeBUuHbftx0foKqLthd32H1ChG2nuBpaj8lks6bBildcNfBpX2vscKszYJh0dswQJloce7FRqdMeURFoORsbNHGkYMy6Q3d9L1yag84Xx5Q11nRV98iWdv_x4KNmGQ4jYK3kdTMnhODXK8zA-HbMxFJ60P9pDa2vln3t3B2P13jpmNzkRnf_IQOQTgNO1yvoIZ786YsIhoazldT_ygV214zhuCk_q1z4r99UjHzWKKBqcqg7tdl5Ix71yaxpIxOAbfiMiH5Pz3GnVC5DTh9X8K3C-FnzwKJ6l1HAH5aJgt88jfTRRxsAANtTsFyYvlQY5i7I5xVFcaP29RmwTaOn5DFI1CBKe48d9wDmbxZPF9i5pmz5B0CWLo_FRAt2hUpHVOn0hcMLHAgLR0xIXIaklELqyD9pXenD4s0JjAXvc3Tp3Bwsbp-X5Z_QQhd2_18kpb4w2fsQ6iZTlRQTkiXKy6RFUE0T41CQO7eoEFSK1Fzuqog7EcGhm27RkWQlt9fEfZwEPMZrg7HrEFp7EuMX5Fku7H0DCA7CL61oi3al-sOwabTVu_u4-F-riNiI3ogwRpIUS-k1fS8uaV0UiaMPjGV4mFzSP7spg3Cms8YfV1wFWoThf-Sa-lO1SDP-YS5HnH00aU-P5Ixvm0AA2D6koEr2WB-BgclnGh3JGNGz23wZKCyk-v-_ob8UbotyF3vQZUbwRcPwLuYXJZSrFl1as0itJHG3v3yQC0fIUPgKmNTiuiw_feF5N75leRyJa3PMGdRMOH5fA2mrQCovbpPXgJ1aZHWHsN7ap21oW4aZMjtoeTzZN2Pk_Ef3EOic-lg4zoaUc_31sa-GgQmUUR_3aA1UoOjeG4eVF6S2K7Jjy1R5_oxp80TmDhfRsANO2X6frGGI5SsHvMC7s4SEzH7YTNp6EM81oSlHfpkRMB0v34Sh8Fg4VgdTeQcMInsaF3eUdbZgBWu4rno3xUS3VhGKgyQFPDWXn2hY08fkHAB2AFyahjDf5VURyzoB5QgRsx9g1ehcDFKbP_GX3FYn3rtX4I1WvEmrTCKKQ2X0h96BWs-4yXy9358E7K8vIBgc-rQw1vKkswmNFUN2EVGMFevHnIVIeAzyy9e9lzgC6xafx9wROhwFH9T6Vn8tSKd-8f5PyGWsIZfvsNQ_4wSQaNYYNH6yIM_BIcXXrp2ZkBG_BzyhYKD06kfXvQu8gnsK7ycUoVIcuYNE7oY34bAT0v2yN1xxQFX3u7jUG2NgyPTmUAyqApRz7dXVn255vXwd-9-Epcz0aMoDy0VDSCI76g_bYOmSIMW_RPLWs8lkc67R0k_UtexdvwOgiJc_qOSAElyEsurksw1xSRs68RHwBbun8KHIeHxCCwcla5xCiwr_O3A1djRh-3yCgrulwAcCocYzwGXUScevqEwjZ0QARGJYZGYyjOMF7TVb4h0F1LVvgxBx_BQoBusLJS_MtmPicxdwZaqItQt06hq_qXB7ZtWCqwB5gLG3iywgF68ImHgSaAR6iggPndmxp8Zh9egdh4M8eXT4oHqPhzV3zL7_jkcrhJXehI3DyJ4eJ23gFxJxosMU8QwhNy-g6GczRGR8EjQkav40O8EBUbsqRZ1QjbsjsA3srATu-8dx70gO_1o_o5jxTpSd81Ri4otRmBfmye4HIP34pRcHJKQzs0wQhCaouKY6TOvNLR3Pxm11qLHzc0gpXFjkKntLYRNUqvNmw_MIDfYUvcsAslrPFTyvnv0CN2BhbHn3s6Sgo1eQFPTW1JQuliST2THtRwqR4fgJ678AHeyM6N6Hi6kLpF4L4hMPYIUaLMkzlOp6_9EgBwaNAs-8scztw4f8mJ_XWMyA1rTksjaYl2ENPWdq7Y0gxRMjeGlIcIROl5edD4w2B0JbDyylRhxlL_S-7v8huHtSkcYXzLUIXeMT5HwnPxzE3J4gOMriLEPFyXlX8rHpYEmPjxztjOxg6nuXdetcKjOO61d8IQKItfPoMiKTKZTbcl2yr0zBZKXfY5zcg-sk_NReIKzOaig_nYFFG67lEfAxHxNshQiYXKrDd833_GJ36m8bSGVyJMlnuF7uv6Go53Jt7le0YbCth",
              "width": 300,
              "height": 300,
              "precision": 1
            },
            "place": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHngsfcpn9-qGNL1nqw-_hUG-iUbaXKNlQ7TOHXGC7Twh8qBagvJYCkHMF_fFPdskF0MUzLzg12Nx48mszbWPQAoMCH49IFdpkPUe4gsKn5SwHivl6i8jhDFmzL1xQT2dAGGjenCxS6hzT9SXpw0ZFffgVw1eMfXCYqPqPSxVvrJpDxktTCJUqfHXvXGYe3-l0C2JhVsdEQfg5z6_8WLujwMxQfuQcbq5Av-FBZa-uCVGwzb-3-NkIWIjW-9sBQ1BKG1I306Sl_pT5__yeejMxLPdCFeaTtPnwrVfzAKzrUySwXDIkRKYOUMcJIenH_m3pvDFry2BZkIx4WnOLKQtI4gPSh1dgOcqMyUdMppafMXiLFtmCU6C9cNlbV6Cgi1fEiMD2OJR6bhRr8SHVzzJxhdTBBwfEIQhocLJLGwWTpD4Pfr9boKFWbOGT1FJmB-HAo86lbntEubB5e5toHDvfyLQEikzAYurgw_UBQd92bV183RMnoKUMLETGh4fF85TCP3bHWxDtHvgRq4Qi6iuR-CfeZbb_MIUobWf3JHSro9AYXAZMwLaewA9x2R3bCuVxgGk3s2zplBD47nuzTa-4Duv2R5v8kQqwmRf44vrb3ZwTgsmqh8RpZDE7-6iss9skgBCC7CTSpsh3tQXJD4Zt-aQZQx-oERBwqIJDi33_HMqLtkdTgImG7J2ngCreJ_lYB2KVJnPM2Qh9w4MY8EuvqGTAZoRYaiqUF2mlVQcGhfl0BWefHHVMwPAqd789k0yeQ5ofA8ChkogJB3Sq6nPhzIN2dSq7VLFsfZcHCOxDf7yY1KK8qOaOUBex2U2fZpHBZDkv08jllFQ4JlNbJWskTufif7OIXY6QVSeI-pZ7PZzTbpGKO9hBwNlf1-Cg209MfIyqsNguIhBXtaHR1z4d3fzRD4tsVQAUIDb7rzE_UI7_jhuvwJ1yAImDcOJyn0Gkr_Z1CgvQVew9x3_4SLMrUFxEduSEQoooy8VZJQuKXWUwoaOftB0Y8LxW7_sJpzjuA0bPU4AlLnThHwwO5qc9vI9O_c7fVHn4vXuLjBTHG2CUnCYEqNKGTIeRMZG_wmkRpK37j2DtZKAIrsc7DS8Eist-e1usqU5olbuwGlK7eSxT1hXyq6CtKK1jc7yM23-8HMwGMJSmLgDzsc3xD5LNaRSpo1fIXWRcaDJDm7HnEN6P2mffAPm2dAGL9Fqih8lkryaFNsMojfy1y_NgFLczDMR0YsBUSgI8S_1N5ccK9Y1kIXsjTPlw3ITi4981G6w6E967LxwtUtDpl4CumlN52Hd-TXaPjEnkAffvBEyLz0hQGDJE1D4WwM9BhbFf4g2VfIU3E2QV3Hh8MmvD4fe8koeOE1ug7V6YBfsYUtInWcyDylW-e5DBgLUnU5yYE6c8MID-TAwuVjzvUVVFZ25JDYi9O4-k8ahgeAZvX41_LELz0tf3gJmmeNm32KZe1y1sM_rdLqvcXUz1rxuc9Kfb1PSE4sC4QhpIez25nWPmBR08OT_XfA34wFwGzw9lMyympx4f0xClOhR5-2w-hgsRJI_afV4PXC3gJTNT7ECfSxjQDJbsFEayCP9BcTGzct2R9CU7g7yt3OiE_teDZTOwIieOA6PwbYp8eUfwrpLbWeh3btFSQyS59MlHM7hIn2-YtFQK3Fx-ZrhL_V3FozodddDJN8dkFdhE0GL3x3nL-NaHzuNDDBnCvEU7zK6Oi93Aow6tfiNcMTBlT3sAUMPjxHx4fihQ9n5QOz29YT--Sf18RS-HHGHcQFx2f8-1q9AC534Ds-wJHlhRn4iW_t_VrAd6AQ43ICXgXVsDrFgHV5yQnLpYVBaqiFNttf1D_pERaGGfUziBDHQwIjsvuauUUhOW6z_ACU6E7Ut4npZH0aC3BmV6c7jl_Amjc4jca2NU3ASGKGR2tjDXgS3JxwK1bZhdN7s4rQT83KpHSzW7zFIbCocL_P2-8OFzsCLiQ0lkJ2oR3lPQ8XSFM_MsUKMTyJD4gig4VqZE67VxESceWUnw5aeHmCFwZIgO0z91_1TWqwpTc3Th2mDxY4C-Hr_lWF9q5WYfFMV4cbfTBNTvR0iYjHocpMpqgJNlfT1rarVhGB2bz8jZVNR87he_-e-oyg8Gb48kcSbYcUO46s4HoRz70p1S8ySF5OVrM7BU69esRIgK7Njm4iz7HWkhm-J5nYxNI9cEkWBkqOLjQzknsDr7_utf2BmuNEk3QH6WJ5HY53oFIvPcWTRF_weEDNPrLIxQfuy4ln6MRxnRHUvCGeHgle8vmOkUwFSOc1MlE7QSk_JLF9hVjmh5m1wewrORKH8GUT43BCkwgU8nEBQ3U8TIWCKkLEoGWPPNddkP8oG9hNVjszSNkATIate_JftQwo_Gh6eABQos7UuAAk5__SBTpnHyQ7ypRO23G2Bsl_cQ8GAqZCzeAtD3sS2RM77d6XxFGyOo_fiAvFaXB8VDTGLHguMjzDFOXEE3FFIis9Gob5pxwh9EUeQ5v0A",
              "width": 70,
              "height": 70,
              "precision": 1
            },
            "placeCover": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHnhMeU6X41_ghG2yCytPJvFdfFeYSWOgc9V9j0NDTdyDgcLpMMJqasO_dzZWjium9iBUDxzS5DBjwOr_btRsMDjtCywd0kVb4lSdw7oYHeVR3mqWO8zDpVPEjC_h4H2vA2CwOzJiaqkTHlalVa7Z5eWCZozfsoYAofEKXC0VjuEaTBhsPkOku9Om_sCrS2znUh4LtJhfUNSz9ewcQ4DMnTHjYbrAYOqKwAxV9bcvOSUUkxc8jiC3swDBu39M5g8zi68Y7I-R5OtgVb-i-rluV5FNqYTa3LFHAJSP7MJSDc7zA0PooRMZW4PPxAWGHDhGNhNW3y-ihhJBU1tMv7f9UYnMSy69sKRKQDcfwPh7fUXhnclGOBxS9bCV3h2RY57OohFCOJOBmWoD3ETn9QxLBUeSRGzPonYxcSLq734Ez8Brr9sNHVLk-COEb_JIm05Hg-5J5Wp_gTfT1z6-8JAubTICQLgQsruYwfx0FOT9mlUlgZbM3yAmcGFRiE8OVE5Se77L3M5gl_mjR58yaXtMhrLMGiWLPkMHYhfcrrOTTHzi8CDoYQOKOoAMFqWGzZpWdFEV_sxBVmGTcTu93sYdY0neOSxtkEXY0_SsYGt4TzdCnTgHes1DRKMmTH_BIz2fMUERmRExuVrh78TEtN8Zx-SxNB3fMgUzoVMbLB8UrnCrz7ht3XClGZFnveFre27HIKxIFbsuY9dTtVwsQFEOTxOAoKrw03gpAD33V_dOuDUGgEWerbB1EaLzGGxvhqyhOr15D32gdBggJu7B2hovx4D92kc4_GMGA9cOPBPRPW1yITCrosM4WSN9pKekXlv3NBNVncxAF3Aio_gsnqef83nfKi9NM-R7wYWsUDuY7uRwjbs3uw0i9iCmT3xwQ79vQeOCOIGAmWtDvmc2xH5qNBaiVJ3domZRQJOKTz4m_WG7jipPD5A0KpBWrDGKCJ_Hc3_4RSjtQWWxVq6OE9G_r2GzMarjIPrK4i4XtecPO0WkArbsHkG1I5GRaX78lq4Am-24Po_BZMjx9y_CqVtuxZIOKedZHvM1UKbODPHyrP1xA2OoEPEruzLu1JaGTLv35DMn3U_jZ_KxQLsuzfbtU1oc-u1vYmTa0Qa84kuLTnejjlg1y-6h5SG0jX6SUl0uolAj6HMR6dtDfaa3xsxrBjaSFg3MEuUz89FZ7tyVj_GaHwtvHXDmKfFX7fDb-VzG4G4qZQr_oiXTda6NUBFMjILTc4rREpu68k9l1SdfqAWGIuTs_hK2EZMyyCz_9F3jCk0I3F_x9DoDpH-AyIqctbP8ucV7LHLGgbdd7DMwTb4RwxFaIWMK2gG-d4SWHboEVnEW_g0z5HIw0qhObsSdQLj_mz8d0Ydps-bd0YorTkazzZp0yU-D51E3Dj7jU25uY-KDiWORaYhgH6YG9S2ZZBdy5n5OcDSQAcDLno727kMpL_svzcP225GlnAD5Of7HYC4ZBfpMUdSQ5Yz-IXEtL1GRsotCsWg6sewFFuVfq7WmQzQv_cNUgiDwiUye540g2G17v89CtXqhpg1Tyhlsh5Jfq4TInjK34BSuDqPw771QUwHJM5Cq6lOvNYTEjxkFtOI2Pg7h58Bzkrps7vbeIlj92NwvIIV6o9QfUYporwSwnguGOuxy5KE3nexxQN6MsgNSeOIR-spTPTQVpv_YJVew9Oz-UjeBUJEq_17HzUC472mOX6GVCUL3zdCJ6yz1Yb0Ld8occpXjJz698LBvDVAgQMjDMxqrIQxHNRcsCBd301Uv_dCl80HDCE1upsyhaP97vg2BtjjCVJxSSmjvdSLOmyVbDJNUswaMLCIBr1ygcwAoktGqiDPdJIaEPcgE9IA0jr3y1AJCoLgd_GWcMuu_qg9ckjYIw0XfgenK38UjjenWCMyy9tMWvu3TkH5Ow3Nxe3MROJmDDgW05MwIxXTy1p0PkgYRsjFL3Q7GPDJbnYm9fWOkOIIl36OYeg828Ew55uvuQybBdaysYkLuz2MhU0kxE6qqosx0hxTcCbX0swZt3uFlkcGB2n_shs6wak_o7-8ydTmQR81jmyvtFoHeeaarLDDVM8VdTGGQD_xz8WCbIZMIu5OedKbHPNvHh4AXjp7R1KASMXncDHfv84rdKzxsIHcJ07e_86vYHFTCLJumK81jl9LUT96AcNxMsvMSyFIR2ruB3efW1v8aNzWipi9-gadiMQKLjU6XjMKqD-hsX_OECvPUfCBJy1-lYA8rR_gvMvdSF1-sIhEcT1GAUEoCwQvbYS_k9bcvG7b30CTfbGFUIrCDej4tpG6zS917ne2zxHojxN2Ae0p_pFCOW4VIXrOlAhSdzdNBb1wwQENYwkNbuPPMReWWXjnlhjN2DD7yRTJy4guvL5YcAtnOae5_IHR5gFed8Kh4vsUSn0nWCy7BljOkvX9Twl6O0kGS6yKymlpxXxUFdn0559YhVh3Pk2XDQ5NYTW50XnMYbHg-jiKX-2AlHNG56q_1w46LZ_l_gCUDFp2Pos",
              "width": 100,
              "height": 100,
              "precision": 1
            },
            "placeCoverXS": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHnhMeX6X41_SxOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
              "width": 103,
              "height": 103,
              "precision": 1
            },
            "placeCoverM": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHnhMCU6X4y_ixOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
              "width": 170,
              "height": 170,
              "precision": 1
            },
            "touchPlace": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHnjcfcqX9aoDhG1zy-tuZ5WtKTLoefPnEtRcjaEivzzjYiAbkJMaKjPM1xVk_wunNnNGzk-DtXBSIIsMnOSsAEjdC7z8E_d68_XcQJkozuSDbIq3SHzT9uN0_i6RUT_dkbAiu5BQyosSX9Q1lrwYBQTwha4ts3dBsoPIzX41jqFbnSgtHfPGiJD2zRPoKs0k4k4pJNsNM8eDR1xOIGMNXkAx0LkQcxmZEQ82tHZ86RR1QNQ8HADWcQOgqT7_5x9CWx2Z_12jdXvRlJzh6poOd0B-a6c6noCm4LfdnOEwz75iY7HK46JaWoD_B4d3H8uUNKN1vi2hl-Pjk1pvDYUdIQjfq94dAlUZcfaeI_mIfqcgvIln2Swwp7FGjq1yMJ6sY7ODWGOT2kkAHXSXBFy6FSYQlb7dgqeSUjCb3D8U_0KY_As8XbA2qgHELsPKihzUoB_bBAruU-VR5e9ewpMOv2EzAGtBYRhpMO5lZtUM2Ab0sIU8jcO34TCQ64y-hu9TiC3YDi6xtmnxBA8jyEst9vPfOkXI3uIls_WsXaCC3k0BY3HacMNZmVJfB1bVD4nWd4KWXf3SRcGDYjse7bfdM3rde_78kMbawlYNIMv63afR_cu2yJ0jFCMk3u3RYQ38MBIB6EOjOHqAPjVEVp4ZNlZhhS6ugHfjo_P6zF6kPyL7nMseHFGESdPXDSPqCr-Woe8KVegO04czd1-f4rEvPYEh4AqC0Nmos6121fds-wcn4ves3qJ0Q6Czil5cda5QOv5rzs1QNQiA97xCqwofxzO9iYfo34PlYWcMH9GTTpwRILIawqD66OBdJcUUrsmUN-GWXLzD9BNA83t_byftMmneW11dM9SrwmZdwGop77dSzQp2qS-glCAnb41TkX1eo7ORWWOSmisjzEXlJW3rJTbhh77N4pYjMpDb_g21L2Npvhn-jWKFeMIH7FAbCuxFEb-Zlsq8MWTB1QwfU1FdDhAh8_kAMzu7U09mlHQcWYXUkERdHpBHIdGhGU5e1A8A-8-Zr92A5NlB9M8D6ggNNMAd6GV47NCUoVfuPEADTb5CIwAo0ULre5BsB9f0rhm0RaEV_8xBZ_AD8SguHYfO8bkceQzdksQo0tQt08q6PLSxz3qVKjyhhuIljZyx0J7tAmNjyBMimujiTUdXJF_LFXRxlg5OgCVh4TE5TX8lDvJIngseX2HkeYPGvaHYC39Uw5-7hCn8U0fB1k_foHK-blIBwcthQyvaIS-mxOdce6WGkKQOHaJFgnDzGiytN56gSy1Jn01yFooRtq7SGHgsxlA_ylf5HwGFMrcs_qFALX4w0TG68CPYKzN-F4b1Xav2dIJXL0_B5mIQkYscbZQsEtjOC78-IabIs-fsc8qLLPdzjng0CD7RBWFl_J2CkF9fogJzSJNxuYri_HS21j3q9YQCFGyfI9dwc0FrLh6XvcK43tutT5OEi_I2n2F6Cv8U8P9LN9oNENfjpT6_wdFtLJMAUmiSw2h5QexkxOTsW8RWU6ff_zH2QDGTez999EyAOE7ZLAwytIhjZaxB6EoNZUJ-eeW5bmAmwVW8PgNDbO4gQiNJUBOKOnF-RRRWXEllVEJU_UxzpSICswsuLvbMEJstOU48Mrb6cWfsMCvJL6TifIuX-T0hBfK3bo4yco6-c_PyyAAziqhw7ydkl3yqN5aQpE6cMoYhkiC7Hz2ULAIqf0nPLEFX2aPm77OoOP6H4o17Z_lMYxVR5u9-g_NsnWFD0-rgUviZA8-Wt0dOilQ3U6fMDkCXc7CSi348dfwSOE8b7w9w13ryZCwwa7i99HLf6ncYjTM043c9z0OinM4ho4IIUHHqSGB8BaaHXQkHVvLn7n-xlBAAwhm9bOZ_Uun-SvyPQNZrsbePklsIvLcALLm3OS9TJNG2zF6SsP_OUPBjyMJgWptBTmVXR5yJdbThVY6tomSB8wLrHszmz3DKTGsNHXCXC7GV_iKL-2920Bxalcj_QUfD932MAjFfnHLCIcpQU3tZMH2VR0bsCTRkEYT9ziIXMWKgCV4-ZP6iqx75XMxxhWmjVf1zadse5JBcGle7DLP3Mhd-XuMCT0xBEDFK8kJKCzBcRqeUnnoHdfLEzX8TxIHBA-mvHyceMGjNek7OQcaZ0cXNgJiZXRZyXJq26E5S5iCFn74wso5OM0NCyCBCWEijLFdkVW7IJcRTJJ0M0eeyM1KrT3wWPuKrnUmdPULm-hIWL5PbaP81wr1JVLku0iUw9z3f8LFtPXHBEhjxIri6oA82tFTvCldGozZ9_5FmM8LhyHyeZ98wOGz73X0yNuqzth0S-2nPtLJ_-SU4fIIm8pbMj4OiDP1i09KaoUEqWQEfF8V2vHu0FHBk7u6BpFKzcMpO7NZNIyofaU7NMZV588bOIDoIjaWgLLpVSk-zltIkTAyycO78s2Aya2CjqMpR__fmdr4rpjRhlY_OcJUj4JKLrK6njIE7z5hMLrN1C3Ln37IrOFy0Yp1IBAv8gyTy1L0A",
              "width": 80,
              "height": 80,
              "precision": 1
            },
            "touchPlaceCard": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/21422/110a009b43a505e1733d48e0a1a95920/140x140_noncrop",
              "width": 140,
              "height": 140,
              "precision": 1
            },
            "touchPlaceCover": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPZEN9onBs1qNCplgIELywJzpTGcG_V1ViOmi3nr4RtFHnh8WU6X03_ghG2yCytPJvFdfFeYSWOgc9V9j0NDTdyDgcLpMMJqasO_dzZWjium9iBUDxzS5DBjwOr_btRsMDjtCywd0kVb4lSdw7oYHeVR3mqWO8zDpVPEjC_h4H2vA2CwOzJiaqkTHlalVa7Z5eWCZozfsoYAofEKXC0VjuEaTBhsPkOku9Om_sCrS2znUh4LtJhfUNSz9ewcQ4DMnTHjYbrAYOqKwAxV9bcvOSUUkxc8jiC3swDBu39M5g8zi68Y7I-R5OtgVb-i-rluV5FNqYTa3LFHAJSP7MJSDc7zA0PooRMZW4PPxAWGHDhGNhNW3y-ihhJBU1tMv7f9UYnMSy69sKRKQDcfwPh7fUXhnclGOBxS9bCV3h2RY57OohFCOJOBmWoD3ETn9QxLBUeSRGzPonYxcSLq734Ez8Brr9sNHVLk-COEb_JIm05Hg-5J5Wp_gTfT1z6-8JAubTICQLgQsruYwfx0FOT9mlUlgZbM3yAmcGFRiE8OVE5Se77L3M5gl_mjR58yaXtMhrLMGiWLPkMHYhfcrrOTTHzi8CDoYQOKOoAMFqWGzZpWdFEV_sxBVmGTcTu93sYdY0neOSxtkEXY0_SsYGt4TzdCnTgHes1DRKMmTH_BIz2fMUERmRExuVrh78TEtN8Zx-SxNB3fMgUzoVMbLB8UrnCrz7ht3XClGZFnveFre27HIKxIFbsuY9dTtVwsQFEOTxOAoKrw03gpAD33V_dOuDUGgEWerbB1EaLzGGxvhqyhOr15D32gdBggJu7B2hovx4D92kc4_GMGA9cOPBPRPW1yITCrosM4WSN9pKekXlv3NBNVncxAF3Aio_gsnqef83nfKi9NM-R7wYWsUDuY7uRwjbs3uw0i9iCmT3xwQ79vQeOCOIGAmWtDvmc2xH5qNBaiVJ3domZRQJOKTz4m_WG7jipPD5A0KpBWrDGKCJ_Hc3_4RSjtQWWxVq6OE9G_r2GzMarjIPrK4i4XtecPO0WkArbsHkG1I5GRaX78lq4Am-24Po_BZMjx9y_CqVtuxZIOKedZHvM1UKbODPHyrP1xA2OoEPEruzLu1JaGTLv35DMn3U_jZ_KxQLsuzfbtU1oc-u1vYmTa0Qa84kuLTnejjlg1y-6h5SG0jX6SUl0uolAj6HMR6dtDfaa3xsxrBjaSFg3MEuUz89FZ7tyVj_GaHwtvHXDmKfFX7fDb-VzG4G4qZQr_oiXTda6NUBFMjILTc4rREpu68k9l1SdfqAWGIuTs_hK2EZMyyCz_9F3jCk0I3F_x9DoDpH-AyIqctbP8ucV7LHLGgbdd7DMwTb4RwxFaIWMK2gG-d4SWHboEVnEW_g0z5HIw0qhObsSdQLj_mz8d0Ydps-bd0YorTkazzZp0yU-D51E3Dj7jU25uY-KDiWORaYhgH6YG9S2ZZBdy5n5OcDSQAcDLno727kMpL_svzcP225GlnAD5Of7HYC4ZBfpMUdSQ5Yz-IXEtL1GRsotCsWg6sewFFuVfq7WmQzQv_cNUgiDwiUye540g2G17v89CtXqhpg1Tyhlsh5Jfq4TInjK34BSuDqPw771QUwHJM5Cq6lOvNYTEjxkFtOI2Pg7h58Bzkrps7vbeIlj92NwvIIV6o9QfUYporwSwnguGOuxy5KE3nexxQN6MsgNSeOIR-spTPTQVpv_YJVew9Oz-UjeBUJEq_17HzUC472mOX6GVCUL3zdCJ6yz1Yb0Ld8occpXjJz698LBvDVAgQMjDMxqrIQxHNRcsCBd301Uv_dCl80HDCE1upsyhaP97vg2BtjjCVJxSSmjvdSLOmyVbDJNUswaMLCIBr1ygcwAoktGqiDPdJIaEPcgE9IA0jr3y1AJCoLgd_GWcMuu_qg9ckjYIw0XfgenK38UjjenWCMyy9tMWvu3TkH5Ow3Nxe3MROJmDDgW05MwIxXTy1p0PkgYRsjFL3Q7GPDJbnYm9fWOkOIIl36OYeg828Ew55uvuQybBdaysYkLuz2MhU0kxE6qqosx0hxTcCbX0swZt3uFlkcGB2n_shs6wak_o7-8ydTmQR81jmyvtFoHeeaarLDDVM8VdTGGQD_xz8WCbIZMIu5OedKbHPNvHh4AXjp7R1KASMXncDHfv84rdKzxsIHcJ07e_86vYHFTCLJumK81jl9LUT96AcNxMsvMSyFIR2ruB3efW1v8aNzWipi9-gadiMQKLjU6XjMKqD-hsX_OECvPUfCBJy1-lYA8rR_gvMvdSF1-sIhEcT1GAUEoCwQvbYS_k9bcvG7b30CTfbGFUIrCDej4tpG6zS917ne2zxHojxN2Ae0p_pFCOW4VIXrOlAhSdzdNBb1wwQENYwkNbuPPMReWWXjnlhjN2DD7yRTJy4guvL5YcAtnOae5_IHR5gFed8Kh4vsUSn0nWCy7BljOkvX9Twl6O0kGS6yKymlpxXxUFdn0559YhVh3Pk2XDQ5NYTW50XnMYbHg-jiKX-2AlHNG56q_1w46LZ_l_gCUDFp2Pos",
              "width": 220,
              "height": 220,
              "precision": 1
            },
            "touchConcertPlace": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/21422/110a009b43a505e1733d48e0a1a95920/s88x88",
              "width": 88,
              "height": 88,
              "precision": 1
            }
          },
          "address": "ул. Большая Никитская, 19/13",
          "type": {
            "id": "5575d419cc1c724f5a8e1151",
            "rubricUrl": "/moscow/theater_place",
            "code": "theater_place",
            "type": "place",
            "status": "approved",
            "name": "театр",
            "namePlural": "театры",
            "nameAcc": "в театр",
            "nameGen": null,
            "nameAdj": null,
            "plural": null,
            "rubricPlacesUrl": "/moscow/theater_place/places"
          },
          "tags": [
            {
              "id": "5575d419cc1c724f5a8e1151",
              "rubricUrl": "/moscow/theater_place",
              "code": "theater_place",
              "type": "place",
              "status": "approved",
              "name": "театр",
              "namePlural": "театры",
              "nameAcc": "в театр",
              "nameGen": null,
              "nameAdj": null,
              "plural": null,
              "rubricPlacesUrl": "/moscow/theater_place/places"
            }
          ],
          "systemTags": [
            {
              "code": "theater_place"
            }
          ],
          "city": {
            "id": "moscow",
            "name": "Москва",
            "geoid": 213,
            "timezone": "Europe/Moscow"
          },
          "metro": [
            {
              "name": "Арбатская",
              "colors": [
                "#003399",
                "#0099cc"
              ]
            },
            {
              "name": "Александровский сад",
              "colors": [
                "#0099cc"
              ]
            }
          ],
          "coordinates": {
            "longitude": 37.60150099999999,
            "latitude": 55.756932999999954
          },
          "bgColor": "#8c3130",
          "logoColor": "#d94c4a",
          "distance": null,
          "isFavorite": true
        },
        "placePreview": "Театр им. Маяковского",
        "placesTotal": 1,
        "preview": {
          "type": "months",
          "text": "Ноябрь, декабрь, январь",
          "singleDate": null,
          "regularity": null
        },
        "collapsedText": null,
        "regularity": {
          "singleShowtime": null,
          "isRegular": false,
          "daily": [],
          "weekly": []
        }
      },
      "distance": null,
      "isPersonal": false,
      "commentsCount": 14
    },
    {
      "event": {
        "id": "557710697abde95fc295586d",
        "url": "/moscow/theatre_show/zhenitba-figaro-teatr-im-pushkina",
        "title": "Женитьба Фигаро",
        "originalTitle": null,
        "dateReleased": null,
        "permanent": false,
        "systemTags": [
          {
            "code": "theatre"
          },
          {
            "code": "theatre_show"
          },
          {
            "code": "tickets-theatre"
          },
          {
            "code": "nearest-events"
          },
          {
            "code": "comedy"
          },
          {
            "code": "newyear-vacations"
          },
          {
            "code": "family-theatre"
          },
          {
            "code": "big-tickets-theatre"
          },
          {
            "code": "traditional-theatre"
          }
        ],
        "argument": "В главной роли Сергей Лазарев",
        "promoArgument": null,
        "contentRating": "16+",
        "kinopoisk": null,
        "userRating": {
          "overall": {
            "value": 9.4,
            "count": 198
          }
        },
        "isFavorite": false,
        "type": {
          "id": "566991d27c650906c42d02b8",
          "code": "theatre",
          "type": "format",
          "status": "reviewed",
          "name": "Театр",
          "plural": {
            "one": "Театр",
            "some": "спектакля",
            "many": "спектаклей",
            "none": null
          },
          "nameCases": {
            "acc": "в театр",
            "gen": "театра"
          }
        },
        "tags": [
          {
            "id": "56bca4bf8323014e3902a6e8",
            "code": "theatre_show",
            "type": "format",
            "status": "approved",
            "name": "Спектакль",
            "plural": null,
            "nameCases": {
              "acc": "на спектакль",
              "gen": "спектакля"
            }
          },
          {
            "id": "57d28482377536932cfc4c2e",
            "code": "comedy",
            "type": "genre",
            "status": "approved",
            "name": "Комедия",
            "plural": null,
            "nameCases": {
              "acc": null,
              "gen": null
            }
          }
        ],
        "image": {
          "subType": null,
          "source": {
            "id": null,
            "title": "teatrpushkin.ru",
            "url": null
          },
          "bgColor": "#3b3835",
          "eventCover": {
            "url": "https://avatars.mds.yandex.net/get-afishanew/35821/ff6f77d0e57357d0d0d81a1c0869fd59/s270x135",
            "width": 270,
            "height": 135,
            "precision": 1
          },
          "eventCoverXS": {
            "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnjMfcp39-qGNL1nqw-_hUG-iUbaXKNlQ7TOHXGC7Twh8qBagvJYCkHMF_fFPdskF0MUzLzg12Nx48mszbWPQAoMCH49IFdpkPUe4gsKn5SwHivl6i8jhDFmzL1xQT2dAGGjenCxS6hzT9SXpw0ZFffgVw1eMfXCYqPqPSxVvrJpDxktTCJUqfHXvXGYe3-l0C2JhVsdEQfg5z6_8WLujwMxQfuQcbq5Av-FBZa-uCVGwzb-3-NkIWIjW-9sBQ1BKG1I306Sl_pT5__yeejMxLPdCFeaTtPnwrVfzAKzrUySwXDIkRKYOUMcJIenH_m3pvDFry2BZkIx4WnOLKQtI4gPSh1dgOcqMyUdMppafMXiLFtmCU6C9cNlbV6Cgi1fEiMD2OJR6bhRr8SHVzzJxhdTBBwfEIQhocLJLGwWTpD4Pfr9boKFWbOGT1FJmB-HAo86lbntEubB5e5toHDvfyLQEikzAYurgw_UBQd92bV183RMnoKUMLETGh4fF85TCP3bHWxDtHvgRq4Qi6iuR-CfeZbb_MIUobWf3JHSro9AYXAZMwLaewA9x2R3bCuVxgGk3s2zplBD47nuzTa-4Duv2R5v8kQqwmRf44vrb3ZwTgsmqh8RpZDE7-6iss9skgBCC7CTSpsh3tQXJD4Zt-aQZQx-oERBwqIJDi33_HMqLtkdTgImG7J2ngCreJ_lYB2KVJnPM2Qh9w4MY8EuvqGTAZoRYaiqUF2mlVQcGhfl0BWefHHVMwPAqd789k0yeQ5ofA8ChkogJB3Sq6nPhzIN2dSq7VLFsfZcHCOxDf7yY1KK8qOaOUBex2U2fZpHBZDkv08jllFQ4JlNbJWskTufif7OIXY6QVSeI-pZ7PZzTbpGKO9hBwNlf1-Cg209MfIyqsNguIhBXtaHR1z4d3fzRD4tsVQAUIDb7rzE_UI7_jhuvwJ1yAImDcOJyn0Gkr_Z1CgvQVew9x3_4SLMrUFxEduSEQoooy8VZJQuKXWUwoaOftB0Y8LxW7_sJpzjuA0bPU4AlLnThHwwO5qc9vI9O_c7fVHn4vXuLjBTHG2CUnCYEqNKGTIeRMZG_wmkRpK37j2DtZKAIrsc7DS8Eist-e1usqU5olbuwGlK7eSxT1hXyq6CtKK1jc7yM23-8HMwGMJSmLgDzsc3xD5LNaRSpo1fIXWRcaDJDm7HnEN6P2mffAPm2dAGL9Fqih8lkryaFNsMojfy1y_NgFLczDMR0YsBUSgI8S_1N5ccK9Y1kIXsjTPlw3ITi4981G6w6E967LxwtUtDpl4CumlN52Hd-TXaPjEnkAffvBEyLz0hQGDJE1D4WwM9BhbFf4g2VfIU3E2QV3Hh8MmvD4fe8koeOE1ug7V6YBfsYUtInWcyDylW-e5DBgLUnU5yYE6c8MID-TAwuVjzvUVVFZ25JDYi9O4-k8ahgeAZvX41_LELz0tf3gJmmeNm32KZe1y1sM_rdLqvcXUz1rxuc9Kfb1PSE4sC4QhpIez25nWPmBR08OT_XfA34wFwGzw9lMyympx4f0xClOhR5-2w-hgsRJI_afV4PXC3gJTNT7ECfSxjQDJbsFEayCP9BcTGzct2R9CU7g7yt3OiE_teDZTOwIieOA6PwbYp8eUfwrpLbWeh3btFSQyS59MlHM7hIn2-YtFQK3Fx-ZrhL_V3FozodddDJN8dkFdhE0GL3x3nL-NaHzuNDDBnCvEU7zK6Oi93Aow6tfiNcMTBlT3sAUMPjxHx4fihQ9n5QOz29YT--Sf18RS-HHGHcQFx2f8-1q9AC534Ds-wJHlhRn4iW_t_VrAd6AQ43ICXgXVsDrFgHV5yQnLpYVBaqiFNttf1D_pERaGGfUziBDHQwIjsvuauUUhOW6z_ACU6E7Ut4npZH0aC3BmV6c7jl_Amjc4jca2NU3ASGKGR2tjDXgS3JxwK1bZhdN7s4rQT83KpHSzW7zFIbCocL_P2-8OFzsCLiQ0lkJ2oR3lPQ8XSFM_MsUKMTyJD4gig4VqZE67VxESceWUnw5aeHmCFwZIgO0z91_1TWqwpTc3Th2mDxY4C-Hr_lWF9q5WYfFMV4cbfTBNTvR0iYjHocpMpqgJNlfT1rarVhGB2bz8jZVNR87he_-e-oyg8Gb48kcSbYcUO46s4HoRz70p1S8ySF5OVrM7BU69esRIgK7Njm4iz7HWkhm-J5nYxNI9cEkWBkqOLjQzknsDr7_utf2BmuNEk3QH6WJ5HY53oFIvPcWTRF_weEDNPrLIxQfuy4ln6MRxnRHUvCGeHgle8vmOkUwFSOc1MlE7QSk_JLF9hVjmh5m1wewrORKH8GUT43BCkwgU8nEBQ3U8TIWCKkLEoGWPPNddkP8oG9hNVjszSNkATIate_JftQwo_Gh6eABQos7UuAAk5__SBTpnHyQ7ypRO23G2Bsl_cQ8GAqZCzeAtD3sS2RM77d6XxFGyOo_fiAvFaXB8VDTGLHguMjzDFOXEE3FFIis9Gob5pxwh9EUeQ5v0A",
            "width": 90,
            "height": 60,
            "precision": 1
          },
          "eventCoverS": {
            "url": "https://afisha.yandex.ru/267GrD643/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnhMeU6Xk1tTEc1yzlp6B6JcSof5HhM1c2f_3hKwrz7Tc4FYsrM5auE_9te2H6gXFaGXvD5SpSFD4cs-vgePYTqd2C1NYMT70AcM0Uv6fyezreolWi5gtZIVLdyysGzuclISW5JBenlDDXUU1n2Y1SRBNP__sHQD4vKLHS_mb1DI_ts8HhHG-BBmLnLYaQ7Hgs3ZhzqfUocRxKwusDBPPWBRQrkTobqIUnzFRURMK3QU8BeeDDGmkgHyC6z9pj_jO7-5bewTdjtDxB4wW4iddOOuKQboXgFF8eb-T8PDnn6jwLKIIKDZqtI9JuTGfYo1hhAkbV3DxJBiocme3Oaew1kf228uAGRLk6Tc0ptrL8Ti_9hV2c0BFOPnLn1RQ6_-sEBQ-zDTmttTL5UExo2pBfehh6zu8VVyATHqPj6mLKDqb-nfzjNmKeAkf4D4uO2noB97NCp9ooTw5a7-YmFdPJBwo-rBAsq5QP01FETd6BWEwyfcvnDHYhAhO-0M1S0gKZ8p_i4xpxjCd79huXrdFmD9a3cpH7NUAoX-j9NQ_31gEhKI8QLJ6JB-BwclrfnnpHDVDCwj9lBw08tO_AcMUJqse_wtMhbok1WdkEp6ntdRbboFmW5Qh7O0j__hY58cg8BzuuOBWHhwX-QUVv6r1YZQRM3-kOWyYVKK_hznzRIJvfr8LhPmiqIlj1GpWg0nwn3phOtdgKVyBbweA6Ls_VHz4PlyIKqaQS5nZtSOidYmUwS9bJI0IxOT6F7MNsyjSO7aTU9S5irzt93Se1rcd6Av-ddrbqLE05W9TBPinN4RoBCqYsNoqNI-ZAck7OhWdrNETE2hZmBxwMhuX6avQuusS6zNk8Xag9atUYobLFTRbrm0-eyg9xEnLm9QQ66-0mOBykLyq4pjP2QWxp3JNEbBJ-zMw_SiIMCoLPx2_hM4rCodXeLm2XGV38JqeL_FIY9L12vsYNdBlLwN8CAPH0ITAukzo9o4w90V1SVOu-VEIhYufJCVgkNS2aytJhxymS_ZPg4T5DgARH2zmcrvJNHvyTVI_zLH8ca-_iHxfs-C0CGIcCNoePJMJISHnGrFlfBGHxzTxkOyEApMDiYOUmi8-dzeM1YJgDWvIWmYP1XDrLtW6A7hFKKG_p3BMx6-EaIAyPDzmapTffQHdh6rhwQShg5_sWSDseGIPhyk_XI57etMrCHnSmBH_-B4m_-nAo9IlKsfQzQh1pw_wkF_DyNhYiljMJoa448VNXZNiefng0QtHmN2E-PiO3ydtu6Ayn-bX9_hlBny1F-Rq0sc9cB8KfeKHnGnMbRMz7PQH_zSczOYISKbyrB9B8ZXH-pEB-MmvC6j1aFRcdg-vcW9MIjdyh1-M2cZw_fuI8i6PSVAL_sn6T2h1RAmn41Bs02dc6Kx-xEB-4uzjYeFFM8IdRWA9lwc0NYwgRHI7q-0DxLLnBtubIPmyiB0nxDLaA7kkq075ct-4OdjF52sYbL_TIABoetjMyo6gl_WNqevGlQlwiRMDbO1wcORWOwu964iyA1IXUwRpjhRxh4iGQttlGOPy2dKvHLmoaTf3UBwL67DMTPKs4GaKCNdx8WFHFgHR_EEPBzgt0FTMjsMTMeuILofSh090iUakGYc0GtLPtVAvCm1-o1DBPH3bgzBIA-uUTCiqMNAustxnxU1NswZJERhl4wt89WhQYNpfM3X3cGZzcsevlHUy7Nm7SCbS0-XUB94NAo8wubS5d4t48Bu3GBDghkQkIjrEj7WNrReazUWQyW8TPI0cVGRWS7t9OxBOpxJ3T2SVIjA9r-xi6qOx3Gt6ea7_JMWgaU-fAFwTc6xIDGKAVCbaEFfd3aWL5o2dfN1Lo-ip_IRQOh__nTcQCvfmn6fouSJg4RM4kuLLKdhnygXKi2BdYHUbZ3B4lx-YgED6vCQWugzvWTE9v2JxuQAtdwsAqdCM2NaXg_m7AFL37gPL3IXWkJUfAFpevy1Ao1ppvi9ANXT9l_fw3BvX6BwMBrgkSpocm2UFYWeCbVUkRc-bPAlc-ECCMxeN-0TKc14DH6QNyvQFDxBqwkPR7J8iaUqXDPFA8WNz0PSfm7ycBHJAENYG0F8d1W1Lzhm5DK03p3RZpNzwdtPTDXdUNm_6DyNYXVoIvY8wUpaTaajbhtEyo-DBAG33rzBAH58seNh2MOCqKljzda15Vz6RdfA5Zx9slezoQKLfJ_G3nC6fDveniKEygFG3RKoCy0mYH5p5qtPgOdy9VzsEdEenEPgQrkTgylrEU8mpwWvusRWMVb_TlAmUnORes7fhq6gqt2b7B8ChfqANh-i2Yp_dmO8CBf7PJOGsuZOLJOBfQ6gQVKYYqF6GvId9fWWvqoGN0DH_Xwil8BggwlcTDatAzmd6z8tw-S4kSRM4an4TEfTnLqXeA1BZLM3_cxiQJ-MMxGyeEGheErgPeQE955bN0YTJbyeYOYBwpLZrU7VL-NLHMouv9LUaYDm_RP4uf93YbxKZ3jMModRtK3tA",
            "width": 100,
            "height": 60,
            "precision": 1
          },
          "eventCoverL": {
            "url": "https://avatars.mds.yandex.net/get-afishanew/35821/ff6f77d0e57357d0d0d81a1c0869fd59/s380x250",
            "width": 380,
            "height": 250,
            "precision": 1
          },
          "eventCoverM": {
            "url": "https://avatars.mds.yandex.net/get-afishanew/35821/ff6f77d0e57357d0d0d81a1c0869fd59/s279x190",
            "width": 279,
            "height": 190,
            "precision": 1
          },
          "featured": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsSdoTc0-2dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
            "width": 390,
            "height": 150,
            "precision": 1
          },
          "featuredSelection": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsOWoTc0-mdT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
            "width": 420,
            "height": 140,
            "precision": 1
          },
          "headingPrimaryS": {
            "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsaWp399-mcYzyjlpf8rD4yUUZP7Pk0bdMDDMhPS2hwfAKEKBKeqGexWWErdk1d-NE3y8j5WPB47kMLOTcoKmMWFxfk6dYkUYscZib_HcQ_elU6J8RR-HEzO1B8z-NoQIgqzEzSVpT3dbHti4aVRXThu7PgKaiIzKbrT-k_zFIbGmuPJC2C-BEL7H5uV_kg4wJZYissydQ9v5ukHLNjyEh87kyY6vbsx0n1seeS8ckYCfefqPHUaLgCk4_JE7jCDzaXX3y5_ni9OziW4kdZ2IfugTrXDL1kaU8jrIgrPzS8LB6o5Oa6LJ-BVaGfepFFcFmTJ6QNABQgggtbOZ8wkid-j_dkOU78eacMjtL_6eBrQoFuq1hxAKlbZyz8J5uUsEwaSNx6fjBPXTXlM4KReXiVj0vM_WzYhPqTvzF3CAIL5mMraJV28Lk_kG76K3EUm9pR1oOADeyBv2PsXAdXXAz8kkTgvgJEG0WxEZuGse1o0ZOTZOF4-OB-l_sFA8Sey4ZT11idDvAJc9j6ChMhZBf2Ie4HkM00BctfdEgbOxBkbO5cTOaORBuRxTFXAmmxbK0bv5hVXGwsMg_HuSs4qkPafxuMHY4w5Q_MsoKvXaQHBm2KM8xhKH0_szgURzecvHSWqNSqCuT_9f05L8a1Zbghkze8JSjA6MqLp-lHAJJzitvf7F2O-JkXQO6GHyVsI_pJTicsPaSJNwNUWL9PLOCM4iQweu6Mg01xZU8aFfmwoXs3bDkMQFyu1xex7zSmM-aLiyRx1qjZP1SKEr_R7BeuUdqjON2oQa9rMFjryzz8hDIwzG4qtHPB1aFPwmnhKMFvD3wFRAyIPg-DeeMQQise41uACbYYkcNIkk6fLbxrpo2K8yA5CMEjm5z8IxvUsBwCwCg2IrgDCXnhD8YRfWCZ4xPk7WRULI6bw2HzuLY_SpebmGXSBNkDtAKSO9Wkj0Lxso-43YjxK4-wGLuzzFh0ZtwI_v7sX2XR2ZO26Ym8LaOrKJ3IQPTGgyf9k6ziB9L_-2StBviZu-h2-qepSBt6jaqvAFVMJa-jpJgHR7gEAFbswCauDHP13b3f4oE9CGWX37yRkFAgNv93SWuEIgNaw5-slbLwtTeIao4DFVyvZsk6c5i9cFFbd3SIH7-InBwyMEh2jjhPgXXxq8J9Xbg1M6cMlciIiIb_iyn3AIK_ktfL6DGudBlncHYaM1EcX1p5co9oLbQ501egkLc_VARwfoCQzurIj21ZzROO_UlwrQtDfB0Q_Awi6wvFJ6DGO25rL3Q1coQFs5TS8i8l6GeOyc5XMOX0dXeTuCSLIzBcTILEBKK6TA8ZTTGXMjUd6EXzW2S5XMwkzkevPfco2u-Ce4fgZdrwuXOYmh5DvRQv-unao4T9PIFrG9yQW5-oiNTqsGQ6dkTXCQ3NtyLl6dDJt8OQgVBQ5CoztznDLEaDCutXlDkeXJkHYHrCD33gowqdehO0daxRJ4cQ0NPXqORglligPmrIY2VBuSNOCTHUQfvTJAVUCDzWYxcdw4wWa0brs8D11ngJO_wWYkPJeHvWoTKvlNXc9af3vABPn9hQWAaUhLYe5M9h6fmnMsGdBNUjX-wZUFz8dkc_xTuUmmtGdzdAZcoI6fNMfmL_VehvBun-VyB50LnfY6jsO_-MWFgiFODugtSHWT1JE47taRSd47vI9VwYJM5Dk5GntN53vj_D4CUq6BWHBL5eg2noc1Zt1oNABfzZp-tsQDO3NEAErkgowvYgi9EloWNODc2IGbczZHlEWFy6R5cdszzWu94XF4CVyhj1l9haSict0AMCZbonNKmMzdv_vHgnz5hIwBoQxCYyUI8x8XkLHgVR9Flv33Bd9Ix4Wpejced4NrfeU0d0fSKU2ZeIhvbz3dhrmmG2l0jN-IlDP6As37-8zKwu2Ii-DiC_Ue3Bj_KdZXClS6OAYVxkeHafK51vBFI7zgtHfOFOoOVjePL6yxVkH575cgckuVypKysooE8_GEBkXkTEQgog43H9tbPGwb2QuaeH6NnMWNj667PJy5Ame4qTw8zhmthtfxxi6tsl-ONiVU5_JE3k5e8fJFTLHzDEKArEzDbyFH_tMXHLFs2R3M1LrwAh8BCIAs8DPStUpveab99o7aYkPe_g2mr7Hawz2hEK25w10AnfX7jAF_-ERCyaIBAyguQDwbndo27ZjSxFh1OUcUgIREr7s-knoFo3UncvnBUi9MGHaDZSj-U4a_ohzsc0raAJJ4NoYIPLsBwUpqDY6vbkY7ElfR9qYbH8Zecv-KmE8NgyjxcVSzBKK2ZzB_QZgrzBy0hqYiP5WD9uIT5fSPm8zf_zbKQz6yQE8B5InOKqrPdtXamrvsV1uFV_c5zpCGx0VgvTia-UpiuOl9foLU4MmZvMLvbzJUSzok02c-jZcLlHcxjIy9dUfFC6nKTaomz3-Vkhr8KdPYQZIydkeXD86CZjV_2T1B7LNot3oGkqiNWviF5aj7EU325hvk_U2UDlv0A",
            "width": 1200,
            "height": 400,
            "precision": 0.95
          },
          "microdata": {
            "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jn2oXN9jRj-jRKgC_so9ZqN9SGWY7PNVkIUNfkPA786g06Jqw5M4qrItN4TnTugm9cBkTg6SlVFz4Vvff7WucJvcWw59s8UpYuctovvqLJcD3-tV62wSJ0KHrX6AEE7vM9CCmICAmpgx7lfm14zZxlaDpazfsDRCM8LKPp-EXBOYzQh_f7AFSEBEvjGKCh33MH2L5NlekfbDda_-o8Nc7GMyA3hAcYvpgb_F12Qt6Xd14lYtDSHXQrNzGH7PN69S-pz6fc9zVupwBj3QGbl8lMD8WSWKnHHUkRTcDXKAn32TAzB5I1MLqGIeR-bFbHuXRhEH328jtBFxQTk-bhfN8pieOG7dA4aKsuT9M6sJfcUxr2i2is1j1UEmTo1DAIz9cXAgCmAiirrR_kcW5lwKJuXQtO3-wdeBUuHbftx0foKqLthd32H1ChG2nuBpaj8lks6bBildcNfBpX2vscKszYJh0dswQJloce7FRqdMeURFoORsbNHGkYMy6Q3d9L1yag84Xx5Q11nRV98iWdv_x4KNmGQ4jYK3kdTMnhODXK8zA-HbMxFJ60P9pDa2vln3t3B2P13jpmNzkRnf_IQOQTgNO1yvoIZ786YsIhoazldT_ygV214zhuCk_q1z4r99UjHzWKKBqcqg7tdl5Ix71yaxpIxOAbfiMiH5Pz3GnVC5DTh9X8K3C-FnzwKJ6l1HAH5aJgt88jfTRRxsAANtTsFyYvlQY5i7I5xVFcaP29RmwTaOn5DFI1CBKe48d9wDmbxZPF9i5pmz5B0CWLo_FRAt2hUpHVOn0hcMLHAgLR0xIXIaklELqyD9pXenD4s0JjAXvc3Tp3Bwsbp-X5Z_QQhd2_18kpb4w2fsQ6iZTlRQTkiXKy6RFUE0T41CQO7eoEFSK1Fzuqog7EcGhm27RkWQlt9fEfZwEPMZrg7HrEFp7EuMX5Fku7H0DCA7CL61oi3al-sOwabTVu_u4-F-riNiI3ogwRpIUS-k1fS8uaV0UiaMPjGV4mFzSP7spg3Cms8YfV1wFWoThf-Sa-lO1SDP-YS5HnH00aU-P5Ixvm0AA2D6koEr2WB-BgclnGh3JGNGz23wZKCyk-v-_ob8UbotyF3vQZUbwRcPwLuYXJZSrFl1as0itJHG3v3yQC0fIUPgKmNTiuiw_feF5N75leRyJa3PMGdRMOH5fA2mrQCovbpPXgJ1aZHWHsN7ap21oW4aZMjtoeTzZN2Pk_Ef3EOic-lg4zoaUc_31sa-GgQmUUR_3aA1UoOjeG4eVF6S2K7Jjy1R5_oxp80TmDhfRsANO2X6frGGI5SsHvMC7s4SEzH7YTNp6EM81oSlHfpkRMB0v34Sh8Fg4VgdTeQcMInsaF3eUdbZgBWu4rno3xUS3VhGKgyQFPDWXn2hY08fkHAB2AFyahjDf5VURyzoB5QgRsx9g1ehcDFKbP_GX3FYn3rtX4I1WvEmrTCKKQ2X0h96BWs-4yXy9358E7K8vIBgc-rQw1vKkswmNFUN2EVGMFevHnIVIeAzyy9e9lzgC6xafx9wROhwFH9T6Vn8tSKd-8f5PyGWsIZfvsNQ_4wSQaNYYNH6yIM_BIcXXrp2ZkBG_BzyhYKD06kfXvQu8gnsK7ycUoVIcuYNE7oY34bAT0v2yN1xxQFX3u7jUG2NgyPTmUAyqApRz7dXVn255vXwd-9-Epcz0aMoDy0VDSCI76g_bYOmSIMW_RPLWs8lkc67R0k_UtexdvwOgiJc_qOSAElyEsurksw1xSRs68RHwBbun8KHIeHxCCwcla5xCiwr_O3A1djRh-3yCgrulwAcCocYzwGXUScevqEwjZ0QARGJYZGYyjOMF7TVb4h0F1LVvgxBx_BQoBusLJS_MtmPicxdwZaqItQt06hq_qXB7ZtWCqwB5gLG3iywgF68ImHgSaAR6iggPndmxp8Zh9egdh4M8eXT4oHqPhzV3zL7_jkcrhJXehI3DyJ4eJ23gFxJxosMU8QwhNy-g6GczRGR8EjQkav40O8EBUbsqRZ1QjbsjsA3srATu-8dx70gO_1o_o5jxTpSd81Ri4otRmBfmye4HIP34pRcHJKQzs0wQhCaouKY6TOvNLR3Pxm11qLHzc0gpXFjkKntLYRNUqvNmw_MIDfYUvcsAslrPFTyvnv0CN2BhbHn3s6Sgo1eQFPTW1JQuliST2THtRwqR4fgJ678AHeyM6N6Hi6kLpF4L4hMPYIUaLMkzlOp6_9EgBwaNAs-8scztw4f8mJ_XWMyA1rTksjaYl2ENPWdq7Y0gxRMjeGlIcIROl5edD4w2B0JbDyylRhxlL_S-7v8huHtSkcYXzLUIXeMT5HwnPxzE3J4gOMriLEPFyXlX8rHpYEmPjxztjOxg6nuXdetcKjOO61d8IQKItfPoMiKTKZTbcl2yr0zBZKXfY5zcg-sk_NReIKzOaig_nYFFG67lEfAxHxNshQiYXKrDd833_GJ36m8bSGVyJMlnuF7uv6Go53Jt7le0YbCth",
            "width": 1200,
            "height": 900,
            "precision": 1
          },
          "suggest": {
            "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsaXoTc8_ixOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
            "width": 130,
            "height": 90,
            "precision": 1
          },
          "type": "image",
          "sizes": {
            "eventCover": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/35821/ff6f77d0e57357d0d0d81a1c0869fd59/s270x135",
              "width": 270,
              "height": 135,
              "precision": 1
            },
            "eventCoverXS": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnjMfcp39-qGNL1nqw-_hUG-iUbaXKNlQ7TOHXGC7Twh8qBagvJYCkHMF_fFPdskF0MUzLzg12Nx48mszbWPQAoMCH49IFdpkPUe4gsKn5SwHivl6i8jhDFmzL1xQT2dAGGjenCxS6hzT9SXpw0ZFffgVw1eMfXCYqPqPSxVvrJpDxktTCJUqfHXvXGYe3-l0C2JhVsdEQfg5z6_8WLujwMxQfuQcbq5Av-FBZa-uCVGwzb-3-NkIWIjW-9sBQ1BKG1I306Sl_pT5__yeejMxLPdCFeaTtPnwrVfzAKzrUySwXDIkRKYOUMcJIenH_m3pvDFry2BZkIx4WnOLKQtI4gPSh1dgOcqMyUdMppafMXiLFtmCU6C9cNlbV6Cgi1fEiMD2OJR6bhRr8SHVzzJxhdTBBwfEIQhocLJLGwWTpD4Pfr9boKFWbOGT1FJmB-HAo86lbntEubB5e5toHDvfyLQEikzAYurgw_UBQd92bV183RMnoKUMLETGh4fF85TCP3bHWxDtHvgRq4Qi6iuR-CfeZbb_MIUobWf3JHSro9AYXAZMwLaewA9x2R3bCuVxgGk3s2zplBD47nuzTa-4Duv2R5v8kQqwmRf44vrb3ZwTgsmqh8RpZDE7-6iss9skgBCC7CTSpsh3tQXJD4Zt-aQZQx-oERBwqIJDi33_HMqLtkdTgImG7J2ngCreJ_lYB2KVJnPM2Qh9w4MY8EuvqGTAZoRYaiqUF2mlVQcGhfl0BWefHHVMwPAqd789k0yeQ5ofA8ChkogJB3Sq6nPhzIN2dSq7VLFsfZcHCOxDf7yY1KK8qOaOUBex2U2fZpHBZDkv08jllFQ4JlNbJWskTufif7OIXY6QVSeI-pZ7PZzTbpGKO9hBwNlf1-Cg209MfIyqsNguIhBXtaHR1z4d3fzRD4tsVQAUIDb7rzE_UI7_jhuvwJ1yAImDcOJyn0Gkr_Z1CgvQVew9x3_4SLMrUFxEduSEQoooy8VZJQuKXWUwoaOftB0Y8LxW7_sJpzjuA0bPU4AlLnThHwwO5qc9vI9O_c7fVHn4vXuLjBTHG2CUnCYEqNKGTIeRMZG_wmkRpK37j2DtZKAIrsc7DS8Eist-e1usqU5olbuwGlK7eSxT1hXyq6CtKK1jc7yM23-8HMwGMJSmLgDzsc3xD5LNaRSpo1fIXWRcaDJDm7HnEN6P2mffAPm2dAGL9Fqih8lkryaFNsMojfy1y_NgFLczDMR0YsBUSgI8S_1N5ccK9Y1kIXsjTPlw3ITi4981G6w6E967LxwtUtDpl4CumlN52Hd-TXaPjEnkAffvBEyLz0hQGDJE1D4WwM9BhbFf4g2VfIU3E2QV3Hh8MmvD4fe8koeOE1ug7V6YBfsYUtInWcyDylW-e5DBgLUnU5yYE6c8MID-TAwuVjzvUVVFZ25JDYi9O4-k8ahgeAZvX41_LELz0tf3gJmmeNm32KZe1y1sM_rdLqvcXUz1rxuc9Kfb1PSE4sC4QhpIez25nWPmBR08OT_XfA34wFwGzw9lMyympx4f0xClOhR5-2w-hgsRJI_afV4PXC3gJTNT7ECfSxjQDJbsFEayCP9BcTGzct2R9CU7g7yt3OiE_teDZTOwIieOA6PwbYp8eUfwrpLbWeh3btFSQyS59MlHM7hIn2-YtFQK3Fx-ZrhL_V3FozodddDJN8dkFdhE0GL3x3nL-NaHzuNDDBnCvEU7zK6Oi93Aow6tfiNcMTBlT3sAUMPjxHx4fihQ9n5QOz29YT--Sf18RS-HHGHcQFx2f8-1q9AC534Ds-wJHlhRn4iW_t_VrAd6AQ43ICXgXVsDrFgHV5yQnLpYVBaqiFNttf1D_pERaGGfUziBDHQwIjsvuauUUhOW6z_ACU6E7Ut4npZH0aC3BmV6c7jl_Amjc4jca2NU3ASGKGR2tjDXgS3JxwK1bZhdN7s4rQT83KpHSzW7zFIbCocL_P2-8OFzsCLiQ0lkJ2oR3lPQ8XSFM_MsUKMTyJD4gig4VqZE67VxESceWUnw5aeHmCFwZIgO0z91_1TWqwpTc3Th2mDxY4C-Hr_lWF9q5WYfFMV4cbfTBNTvR0iYjHocpMpqgJNlfT1rarVhGB2bz8jZVNR87he_-e-oyg8Gb48kcSbYcUO46s4HoRz70p1S8ySF5OVrM7BU69esRIgK7Njm4iz7HWkhm-J5nYxNI9cEkWBkqOLjQzknsDr7_utf2BmuNEk3QH6WJ5HY53oFIvPcWTRF_weEDNPrLIxQfuy4ln6MRxnRHUvCGeHgle8vmOkUwFSOc1MlE7QSk_JLF9hVjmh5m1wewrORKH8GUT43BCkwgU8nEBQ3U8TIWCKkLEoGWPPNddkP8oG9hNVjszSNkATIate_JftQwo_Gh6eABQos7UuAAk5__SBTpnHyQ7ypRO23G2Bsl_cQ8GAqZCzeAtD3sS2RM77d6XxFGyOo_fiAvFaXB8VDTGLHguMjzDFOXEE3FFIis9Gob5pxwh9EUeQ5v0A",
              "width": 90,
              "height": 60,
              "precision": 1
            },
            "eventCoverS": {
              "url": "https://afisha.yandex.ru/267GrD643/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnhMeU6Xk1tTEc1yzlp6B6JcSof5HhM1c2f_3hKwrz7Tc4FYsrM5auE_9te2H6gXFaGXvD5SpSFD4cs-vgePYTqd2C1NYMT70AcM0Uv6fyezreolWi5gtZIVLdyysGzuclISW5JBenlDDXUU1n2Y1SRBNP__sHQD4vKLHS_mb1DI_ts8HhHG-BBmLnLYaQ7Hgs3ZhzqfUocRxKwusDBPPWBRQrkTobqIUnzFRURMK3QU8BeeDDGmkgHyC6z9pj_jO7-5bewTdjtDxB4wW4iddOOuKQboXgFF8eb-T8PDnn6jwLKIIKDZqtI9JuTGfYo1hhAkbV3DxJBiocme3Oaew1kf228uAGRLk6Tc0ptrL8Ti_9hV2c0BFOPnLn1RQ6_-sEBQ-zDTmttTL5UExo2pBfehh6zu8VVyATHqPj6mLKDqb-nfzjNmKeAkf4D4uO2noB97NCp9ooTw5a7-YmFdPJBwo-rBAsq5QP01FETd6BWEwyfcvnDHYhAhO-0M1S0gKZ8p_i4xpxjCd79huXrdFmD9a3cpH7NUAoX-j9NQ_31gEhKI8QLJ6JB-BwclrfnnpHDVDCwj9lBw08tO_AcMUJqse_wtMhbok1WdkEp6ntdRbboFmW5Qh7O0j__hY58cg8BzuuOBWHhwX-QUVv6r1YZQRM3-kOWyYVKK_hznzRIJvfr8LhPmiqIlj1GpWg0nwn3phOtdgKVyBbweA6Ls_VHz4PlyIKqaQS5nZtSOidYmUwS9bJI0IxOT6F7MNsyjSO7aTU9S5irzt93Se1rcd6Av-ddrbqLE05W9TBPinN4RoBCqYsNoqNI-ZAck7OhWdrNETE2hZmBxwMhuX6avQuusS6zNk8Xag9atUYobLFTRbrm0-eyg9xEnLm9QQ66-0mOBykLyq4pjP2QWxp3JNEbBJ-zMw_SiIMCoLPx2_hM4rCodXeLm2XGV38JqeL_FIY9L12vsYNdBlLwN8CAPH0ITAukzo9o4w90V1SVOu-VEIhYufJCVgkNS2aytJhxymS_ZPg4T5DgARH2zmcrvJNHvyTVI_zLH8ca-_iHxfs-C0CGIcCNoePJMJISHnGrFlfBGHxzTxkOyEApMDiYOUmi8-dzeM1YJgDWvIWmYP1XDrLtW6A7hFKKG_p3BMx6-EaIAyPDzmapTffQHdh6rhwQShg5_sWSDseGIPhyk_XI57etMrCHnSmBH_-B4m_-nAo9IlKsfQzQh1pw_wkF_DyNhYiljMJoa448VNXZNiefng0QtHmN2E-PiO3ydtu6Ayn-bX9_hlBny1F-Rq0sc9cB8KfeKHnGnMbRMz7PQH_zSczOYISKbyrB9B8ZXH-pEB-MmvC6j1aFRcdg-vcW9MIjdyh1-M2cZw_fuI8i6PSVAL_sn6T2h1RAmn41Bs02dc6Kx-xEB-4uzjYeFFM8IdRWA9lwc0NYwgRHI7q-0DxLLnBtubIPmyiB0nxDLaA7kkq075ct-4OdjF52sYbL_TIABoetjMyo6gl_WNqevGlQlwiRMDbO1wcORWOwu964iyA1IXUwRpjhRxh4iGQttlGOPy2dKvHLmoaTf3UBwL67DMTPKs4GaKCNdx8WFHFgHR_EEPBzgt0FTMjsMTMeuILofSh090iUakGYc0GtLPtVAvCm1-o1DBPH3bgzBIA-uUTCiqMNAustxnxU1NswZJERhl4wt89WhQYNpfM3X3cGZzcsevlHUy7Nm7SCbS0-XUB94NAo8wubS5d4t48Bu3GBDghkQkIjrEj7WNrReazUWQyW8TPI0cVGRWS7t9OxBOpxJ3T2SVIjA9r-xi6qOx3Gt6ea7_JMWgaU-fAFwTc6xIDGKAVCbaEFfd3aWL5o2dfN1Lo-ip_IRQOh__nTcQCvfmn6fouSJg4RM4kuLLKdhnygXKi2BdYHUbZ3B4lx-YgED6vCQWugzvWTE9v2JxuQAtdwsAqdCM2NaXg_m7AFL37gPL3IXWkJUfAFpevy1Ao1ppvi9ANXT9l_fw3BvX6BwMBrgkSpocm2UFYWeCbVUkRc-bPAlc-ECCMxeN-0TKc14DH6QNyvQFDxBqwkPR7J8iaUqXDPFA8WNz0PSfm7ycBHJAENYG0F8d1W1Lzhm5DK03p3RZpNzwdtPTDXdUNm_6DyNYXVoIvY8wUpaTaajbhtEyo-DBAG33rzBAH58seNh2MOCqKljzda15Vz6RdfA5Zx9slezoQKLfJ_G3nC6fDveniKEygFG3RKoCy0mYH5p5qtPgOdy9VzsEdEenEPgQrkTgylrEU8mpwWvusRWMVb_TlAmUnORes7fhq6gqt2b7B8ChfqANh-i2Yp_dmO8CBf7PJOGsuZOLJOBfQ6gQVKYYqF6GvId9fWWvqoGN0DH_Xwil8BggwlcTDatAzmd6z8tw-S4kSRM4an4TEfTnLqXeA1BZLM3_cxiQJ-MMxGyeEGheErgPeQE955bN0YTJbyeYOYBwpLZrU7VL-NLHMouv9LUaYDm_RP4uf93YbxKZ3jMModRtK3tA",
              "width": 100,
              "height": 60,
              "precision": 1
            },
            "eventCoverL": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsScoTc3-2dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
              "width": 380,
              "height": 250,
              "precision": 1
            },
            "eventCoverM": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsWTqDc092dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
              "width": 279,
              "height": 190,
              "precision": 1
            },
            "featured": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsSdoTc0-2dT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
              "width": 390,
              "height": 150,
              "precision": 1
            },
            "featuredSelection": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsOWoTc0-mdT0nqypKl-U9S6b7_HLHkwccPOAQ_k6Tg_L4kYFISuD_pcV3TPlGVZB33c2gleFzkfs-LuZO0xuMeWzOQ_Qo0dW-MWqJzzfgHVpXW17R9-CH_U4yEl5OUFNT2QKCaLij7Af39I-ZJGVSRj1u41QDorNaLW7F3zL7vYsPzVKnWdPWflBIKlykkf1rN2j8sUbStX6fs-BcznOAQdpSYOlYYx0WhkTeCxXW83aMTYKngnAiuS3udA1yqw54Tq8DVVtjFS3yeGjfRQJOClSYfWOHgXeeveGBLz2iw4JLolHaWQA_lsenf4kkd7LkbH5x9nASINp-LEYsMgouGu7NAZdIcWX9krqKH6aw_gsFaS5SFIEmjLwxs729k0ORy0AiyipDThfVFJ-J1FSCld3dsEVCg8K57g_mznK4Tame_7F3e3MHjhIZ2Hx1cp1J5cpPoaQitp--sTCOn2GBsfuzMzv7EywEB7SPC4QVkua_fcAVwxHSqP7eNfwBuc1qbj-Ql3myNqxB2Tk9t0IsiQfaDKLGM2Zt3uFBP67DwEGZAlEL-xB91ISGnGr0BGDGDI8Qh5Ag4MgMLpYM05i92V1tkpR6A8b9Y_vIzrcB7biXC34St9C13O-QMQ2do6GiS2NjGXiB7TSlZY8Zp1ZS5Cwe0VUjMwLZjW8m7DNZ_0pM7JKXW_OkzBPpCS2Xkh0rh1j_YIQAlx1eo9DvXNBAcHjwIIjZcw8F1Ob9m9d0UUQvXqHHIeKTq0wNhjziWE4LH8wj9hrzBJ2Bu4r_l0NNSdVIrOC3Iva8zqKC_xygYzArAHOYOrE9lsTlnGu1FdEUzx5Q5hKw0MkfLbavcjuvqF1dwnTb0PTt4MsJDtazbjiUCM9yNSDFfnwxoby9kgPz6JETuAtyHyfF5Y2JxDSzJL198GdwIhKYH030DKJq_ntdPHPkqvP3H6O5mu61IP_Idfqs4DXg5S7Po8Mc3jOiY5gSMMlaA62HJ5ROahdGYiZeTDLXI0My-408dF3yiJ_a3s9Qt1vxFm5yG-sdB3AeOBV4TsMmsvWenaEwzQ9CcqNbMVGK2rHttralH8jFl0L3jBwDt2AQ8wrP75T-8pq_K03vsmd7QyfuA8l57VWgbypWCi1j12Emzd3hUy3NIgMwKRARCgpAPxeHdZw5R1YAZm7cEtQCsjMJPm3m7HBpn3oc_SIVafJkDnGZuPxWYJ3rdfnvIMbDBk6Ng_Euv0OyAupy8JnJQ4-ndZSuORR0YIX_HjG10KCjWz3epG1iem2Jjo0xZqmBN5ziOckvhoPPKYaYjAHH8ZVe71MBXy4jQfP4I0Hb20Jf9IeGXRhGF8Nln3yghRADEemuPeZNESndyyzcc8d7cjetwYh7THeiH6nVSlxi5CHnf32AQ61NcSBSKaEi6_giHvd3Bh5blvXyd_ysQLdjAIA5zi02X2Cb_4htDQDVy_PkTkL5SE-lkd57V4qeQKdg1QxMgmKNTMPxoYqxMpnK86_GpVet6Pbn00e-flCmAGNxe069NN4jOs-L_F4z9VmzFj_weHqdxvKuinV6HMFl8tTO_8ATrI4TE-K6IxNJeEO9Z6dGXspFpYAljV4gt1Nh8evt3tS8EzrN-e5cc4SaMDT-UHqI74ah76lGmM5xVMM2nqxxwi3eMxNwu7JxObljXjVllK55leSjJh3NkIZAAxH5XIykPQNJLNo83XAHGcHl3VCLeB-G0K255clPgeVC1L2-weMPPlJhQciSwOppUX5WxFet-weWsnQ_f6DnQeLB6U689h0geKx5bV-zhNpBpq7A2ekPZxH9mFdYnTAlEyTu_iGy7Y5xc5CrIVP7qUL9BaX27dl2Z7EXjy8yJBFxQqmfDacOoEitaC6MECbq8aftsiq6z0aznYhlmWyh9AFH7o9yUy0cYMNDihMzCmmDfXdH5V-5pHRBhnzvwIexcfKLvL-G_zJ47AgurmGWOgJ0LGIaWe23Y4_rd9jdc2SA57ytQBEvjlPigfsgwxpo8_02lxWOysf0MjbtTSLHQ_PDWd3tFK7jef5qPG5ix9giBb4iWhkvxJB9W4Y43qGFs_dsnpIBryxC09P7ARD6uoGOBYb2zvp2xeGGTu7CNmKwI8sePpe84Um9mk7-UjQpYEZMwFqZzpfSnEqUqj9BVgM2buzBci3-QsGQaHEBOXtxPCc3Vy6qBQfCtby_gNYBgQMZ3W6kbxJKnfmNLbAnapHkb3C7SizGshyJhNidIJYA1R2uQyL9LyIhYmtSYOl68P5Vtac8SvZHQzRNDOPl4_Diy06fFi9SOk3pLI2CpkqQ1O4AefpdR-BMika5bHDlE7TdvVHif39Bs4HKQkGYWKOPtud0btnnV4FVPJ3h15FBcNhc7IS84jnuemz9UZSL8Zb_Eiq5LTXTfTpmC-zz1MFW3GziAo6-ozESmqKhu1ih36THZZ-4x6awJG9_oDXTMLF6TTx1vgG7Dgjt3EAGmsFH7tCbS3x0YE2IRvsc8xWyth",
              "width": 420,
              "height": 140,
              "precision": 1
            },
            "headingPrimaryS": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jnxsaWp399-mcYzyjlpf8rD4yUUZP7Pk0bdMDDMhPS2hwfAKEKBKeqGexWWErdk1d-NE3y8j5WPB47kMLOTcoKmMWFxfk6dYkUYscZib_HcQ_elU6J8RR-HEzO1B8z-NoQIgqzEzSVpT3dbHti4aVRXThu7PgKaiIzKbrT-k_zFIbGmuPJC2C-BEL7H5uV_kg4wJZYissydQ9v5ukHLNjyEh87kyY6vbsx0n1seeS8ckYCfefqPHUaLgCk4_JE7jCDzaXX3y5_ni9OziW4kdZ2IfugTrXDL1kaU8jrIgrPzS8LB6o5Oa6LJ-BVaGfepFFcFmTJ6QNABQgggtbOZ8wkid-j_dkOU78eacMjtL_6eBrQoFuq1hxAKlbZyz8J5uUsEwaSNx6fjBPXTXlM4KReXiVj0vM_WzYhPqTvzF3CAIL5mMraJV28Lk_kG76K3EUm9pR1oOADeyBv2PsXAdXXAz8kkTgvgJEG0WxEZuGse1o0ZOTZOF4-OB-l_sFA8Sey4ZT11idDvAJc9j6ChMhZBf2Ie4HkM00BctfdEgbOxBkbO5cTOaORBuRxTFXAmmxbK0bv5hVXGwsMg_HuSs4qkPafxuMHY4w5Q_MsoKvXaQHBm2KM8xhKH0_szgURzecvHSWqNSqCuT_9f05L8a1Zbghkze8JSjA6MqLp-lHAJJzitvf7F2O-JkXQO6GHyVsI_pJTicsPaSJNwNUWL9PLOCM4iQweu6Mg01xZU8aFfmwoXs3bDkMQFyu1xex7zSmM-aLiyRx1qjZP1SKEr_R7BeuUdqjON2oQa9rMFjryzz8hDIwzG4qtHPB1aFPwmnhKMFvD3wFRAyIPg-DeeMQQise41uACbYYkcNIkk6fLbxrpo2K8yA5CMEjm5z8IxvUsBwCwCg2IrgDCXnhD8YRfWCZ4xPk7WRULI6bw2HzuLY_SpebmGXSBNkDtAKSO9Wkj0Lxso-43YjxK4-wGLuzzFh0ZtwI_v7sX2XR2ZO26Ym8LaOrKJ3IQPTGgyf9k6ziB9L_-2StBviZu-h2-qepSBt6jaqvAFVMJa-jpJgHR7gEAFbswCauDHP13b3f4oE9CGWX37yRkFAgNv93SWuEIgNaw5-slbLwtTeIao4DFVyvZsk6c5i9cFFbd3SIH7-InBwyMEh2jjhPgXXxq8J9Xbg1M6cMlciIiIb_iyn3AIK_ktfL6DGudBlncHYaM1EcX1p5co9oLbQ501egkLc_VARwfoCQzurIj21ZzROO_UlwrQtDfB0Q_Awi6wvFJ6DGO25rL3Q1coQFs5TS8i8l6GeOyc5XMOX0dXeTuCSLIzBcTILEBKK6TA8ZTTGXMjUd6EXzW2S5XMwkzkevPfco2u-Ce4fgZdrwuXOYmh5DvRQv-unao4T9PIFrG9yQW5-oiNTqsGQ6dkTXCQ3NtyLl6dDJt8OQgVBQ5CoztznDLEaDCutXlDkeXJkHYHrCD33gowqdehO0daxRJ4cQ0NPXqORglligPmrIY2VBuSNOCTHUQfvTJAVUCDzWYxcdw4wWa0brs8D11ngJO_wWYkPJeHvWoTKvlNXc9af3vABPn9hQWAaUhLYe5M9h6fmnMsGdBNUjX-wZUFz8dkc_xTuUmmtGdzdAZcoI6fNMfmL_VehvBun-VyB50LnfY6jsO_-MWFgiFODugtSHWT1JE47taRSd47vI9VwYJM5Dk5GntN53vj_D4CUq6BWHBL5eg2noc1Zt1oNABfzZp-tsQDO3NEAErkgowvYgi9EloWNODc2IGbczZHlEWFy6R5cdszzWu94XF4CVyhj1l9haSict0AMCZbonNKmMzdv_vHgnz5hIwBoQxCYyUI8x8XkLHgVR9Flv33Bd9Ix4Wpejced4NrfeU0d0fSKU2ZeIhvbz3dhrmmG2l0jN-IlDP6As37-8zKwu2Ii-DiC_Ue3Bj_KdZXClS6OAYVxkeHafK51vBFI7zgtHfOFOoOVjePL6yxVkH575cgckuVypKysooE8_GEBkXkTEQgog43H9tbPGwb2QuaeH6NnMWNj667PJy5Ame4qTw8zhmthtfxxi6tsl-ONiVU5_JE3k5e8fJFTLHzDEKArEzDbyFH_tMXHLFs2R3M1LrwAh8BCIAs8DPStUpveab99o7aYkPe_g2mr7Hawz2hEK25w10AnfX7jAF_-ERCyaIBAyguQDwbndo27ZjSxFh1OUcUgIREr7s-knoFo3UncvnBUi9MGHaDZSj-U4a_ohzsc0raAJJ4NoYIPLsBwUpqDY6vbkY7ElfR9qYbH8Zecv-KmE8NgyjxcVSzBKK2ZzB_QZgrzBy0hqYiP5WD9uIT5fSPm8zf_zbKQz6yQE8B5InOKqrPdtXamrvsV1uFV_c5zpCGx0VgvTia-UpiuOl9foLU4MmZvMLvbzJUSzok02c-jZcLlHcxjIy9dUfFC6nKTaomz3-Vkhr8KdPYQZIydkeXD86CZjV_2T1B7LNot3oGkqiNWviF5aj7EU325hvk_U2UDlv0A",
              "width": 1200,
              "height": 400,
              "precision": 0.95
            },
            "microdata": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8znphpca-PMxR7pXdri_EToA4OFb6xJmlQTp26DgExa2Hgnu1Ms1jn2oXN9jRj-jRKgC_so9ZqN9SGWY7PNVkIUNfkPA786g06Jqw5M4qrItN4TnTugm9cBkTg6SlVFz4Vvff7WucJvcWw59s8UpYuctovvqLJcD3-tV62wSJ0KHrX6AEE7vM9CCmICAmpgx7lfm14zZxlaDpazfsDRCM8LKPp-EXBOYzQh_f7AFSEBEvjGKCh33MH2L5NlekfbDda_-o8Nc7GMyA3hAcYvpgb_F12Qt6Xd14lYtDSHXQrNzGH7PN69S-pz6fc9zVupwBj3QGbl8lMD8WSWKnHHUkRTcDXKAn32TAzB5I1MLqGIeR-bFbHuXRhEH328jtBFxQTk-bhfN8pieOG7dA4aKsuT9M6sJfcUxr2i2is1j1UEmTo1DAIz9cXAgCmAiirrR_kcW5lwKJuXQtO3-wdeBUuHbftx0foKqLthd32H1ChG2nuBpaj8lks6bBildcNfBpX2vscKszYJh0dswQJloce7FRqdMeURFoORsbNHGkYMy6Q3d9L1yag84Xx5Q11nRV98iWdv_x4KNmGQ4jYK3kdTMnhODXK8zA-HbMxFJ60P9pDa2vln3t3B2P13jpmNzkRnf_IQOQTgNO1yvoIZ786YsIhoazldT_ygV214zhuCk_q1z4r99UjHzWKKBqcqg7tdl5Ix71yaxpIxOAbfiMiH5Pz3GnVC5DTh9X8K3C-FnzwKJ6l1HAH5aJgt88jfTRRxsAANtTsFyYvlQY5i7I5xVFcaP29RmwTaOn5DFI1CBKe48d9wDmbxZPF9i5pmz5B0CWLo_FRAt2hUpHVOn0hcMLHAgLR0xIXIaklELqyD9pXenD4s0JjAXvc3Tp3Bwsbp-X5Z_QQhd2_18kpb4w2fsQ6iZTlRQTkiXKy6RFUE0T41CQO7eoEFSK1Fzuqog7EcGhm27RkWQlt9fEfZwEPMZrg7HrEFp7EuMX5Fku7H0DCA7CL61oi3al-sOwabTVu_u4-F-riNiI3ogwRpIUS-k1fS8uaV0UiaMPjGV4mFzSP7spg3Cms8YfV1wFWoThf-Sa-lO1SDP-YS5HnH00aU-P5Ixvm0AA2D6koEr2WB-BgclnGh3JGNGz23wZKCyk-v-_ob8UbotyF3vQZUbwRcPwLuYXJZSrFl1as0itJHG3v3yQC0fIUPgKmNTiuiw_feF5N75leRyJa3PMGdRMOH5fA2mrQCovbpPXgJ1aZHWHsN7ap21oW4aZMjtoeTzZN2Pk_Ef3EOic-lg4zoaUc_31sa-GgQmUUR_3aA1UoOjeG4eVF6S2K7Jjy1R5_oxp80TmDhfRsANO2X6frGGI5SsHvMC7s4SEzH7YTNp6EM81oSlHfpkRMB0v34Sh8Fg4VgdTeQcMInsaF3eUdbZgBWu4rno3xUS3VhGKgyQFPDWXn2hY08fkHAB2AFyahjDf5VURyzoB5QgRsx9g1ehcDFKbP_GX3FYn3rtX4I1WvEmrTCKKQ2X0h96BWs-4yXy9358E7K8vIBgc-rQw1vKkswmNFUN2EVGMFevHnIVIeAzyy9e9lzgC6xafx9wROhwFH9T6Vn8tSKd-8f5PyGWsIZfvsNQ_4wSQaNYYNH6yIM_BIcXXrp2ZkBG_BzyhYKD06kfXvQu8gnsK7ycUoVIcuYNE7oY34bAT0v2yN1xxQFX3u7jUG2NgyPTmUAyqApRz7dXVn255vXwd-9-Epcz0aMoDy0VDSCI76g_bYOmSIMW_RPLWs8lkc67R0k_UtexdvwOgiJc_qOSAElyEsurksw1xSRs68RHwBbun8KHIeHxCCwcla5xCiwr_O3A1djRh-3yCgrulwAcCocYzwGXUScevqEwjZ0QARGJYZGYyjOMF7TVb4h0F1LVvgxBx_BQoBusLJS_MtmPicxdwZaqItQt06hq_qXB7ZtWCqwB5gLG3iywgF68ImHgSaAR6iggPndmxp8Zh9egdh4M8eXT4oHqPhzV3zL7_jkcrhJXehI3DyJ4eJ23gFxJxosMU8QwhNy-g6GczRGR8EjQkav40O8EBUbsqRZ1QjbsjsA3srATu-8dx70gO_1o_o5jxTpSd81Ri4otRmBfmye4HIP34pRcHJKQzs0wQhCaouKY6TOvNLR3Pxm11qLHzc0gpXFjkKntLYRNUqvNmw_MIDfYUvcsAslrPFTyvnv0CN2BhbHn3s6Sgo1eQFPTW1JQuliST2THtRwqR4fgJ678AHeyM6N6Hi6kLpF4L4hMPYIUaLMkzlOp6_9EgBwaNAs-8scztw4f8mJ_XWMyA1rTksjaYl2ENPWdq7Y0gxRMjeGlIcIROl5edD4w2B0JbDyylRhxlL_S-7v8huHtSkcYXzLUIXeMT5HwnPxzE3J4gOMriLEPFyXlX8rHpYEmPjxztjOxg6nuXdetcKjOO61d8IQKItfPoMiKTKZTbcl2yr0zBZKXfY5zcg-sk_NReIKzOaig_nYFFG67lEfAxHxNshQiYXKrDd833_GJ36m8bSGVyJMlnuF7uv6Go53Jt7le0YbCth",
              "width": 1200,
              "height": 900,
              "precision": 1
            },
            "suggest": {
              "url": "https://avatars.mds.yandex.net/get-afishanew/35821/ff6f77d0e57357d0d0d81a1c0869fd59/s130x90",
              "width": 130,
              "height": 90,
              "precision": 1
            }
          }
        },
        "tickets": [
          {
            "id": "11845",
            "price": {
              "currency": "rub",
              "min": 50000,
              "max": 500000
            },
            "discountPercents": []
          },
          {
            "id": "11845",
            "price": {
              "currency": "rub",
              "min": 50000,
              "max": 500000
            },
            "discountPercents": []
          }
        ]
      },
      "scheduleInfo": {
        "dates": [
          "2118-10-21",
          "2118-10-22",
          "2118-10-23",
          "2118-10-24"
        ],
        "dateStarted": "2018-01-08",
        "dateEnd": "2019-01-30",
        "dateReleased": null,
        "permanent": false,
        "onlyPlace": {
          "id": "55b9091f685ae0137059c3b7",
          "url": "/moscow/theatre/places/teatr-im-pushkina",
          "title": "Театр им. Пушкина",
          "logo": {
            "bgColor": "#9c3f30",
            "microdata": {
              "url": "https://afisha.yandex.ru/267GrD337/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLn2oXN9jRj-jRKgC_so9ZqN9SGWY7PNVkIUNfkPA786g06Jqw5M4qrItN4TnTugm9cBkTg6SlVFz4Vvff7WucJvcWw59s8UpYuctovvqLJcD3-tV62wSJ0KHrX6AEE7vM9CCmICAmpgx7lfm14zZxlaDpazfsDRCM8LKPp-EXBOYzQh_f7AFSEBEvjGKCh33MH2L5NlekfbDda_-o8Nc7GMyA3hAcYvpgb_F12Qt6Xd14lYtDSHXQrNzGH7PN69S-pz6fc9zVupwBj3QGbl8lMD8WSWKnHHUkRTcDXKAn32TAzB5I1MLqGIeR-bFbHuXRhEH328jtBFxQTk-bhfN8pieOG7dA4aKsuT9M6sJfcUxr2i2is1j1UEmTo1DAIz9cXAgCmAiirrR_kcW5lwKJuXQtO3-wdeBUuHbftx0foKqLthd32H1ChG2nuBpaj8lks6bBildcNfBpX2vscKszYJh0dswQJloce7FRqdMeURFoORsbNHGkYMy6Q3d9L1yag84Xx5Q11nRV98iWdv_x4KNmGQ4jYK3kdTMnhODXK8zA-HbMxFJ60P9pDa2vln3t3B2P13jpmNzkRnf_IQOQTgNO1yvoIZ786YsIhoazldT_ygV214zhuCk_q1z4r99UjHzWKKBqcqg7tdl5Ix71yaxpIxOAbfiMiH5Pz3GnVC5DTh9X8K3C-FnzwKJ6l1HAH5aJgt88jfTRRxsAANtTsFyYvlQY5i7I5xVFcaP29RmwTaOn5DFI1CBKe48d9wDmbxZPF9i5pmz5B0CWLo_FRAt2hUpHVOn0hcMLHAgLR0xIXIaklELqyD9pXenD4s0JjAXvc3Tp3Bwsbp-X5Z_QQhd2_18kpb4w2fsQ6iZTlRQTkiXKy6RFUE0T41CQO7eoEFSK1Fzuqog7EcGhm27RkWQlt9fEfZwEPMZrg7HrEFp7EuMX5Fku7H0DCA7CL61oi3al-sOwabTVu_u4-F-riNiI3ogwRpIUS-k1fS8uaV0UiaMPjGV4mFzSP7spg3Cms8YfV1wFWoThf-Sa-lO1SDP-YS5HnH00aU-P5Ixvm0AA2D6koEr2WB-BgclnGh3JGNGz23wZKCyk-v-_ob8UbotyF3vQZUbwRcPwLuYXJZSrFl1as0itJHG3v3yQC0fIUPgKmNTiuiw_feF5N75leRyJa3PMGdRMOH5fA2mrQCovbpPXgJ1aZHWHsN7ap21oW4aZMjtoeTzZN2Pk_Ef3EOic-lg4zoaUc_31sa-GgQmUUR_3aA1UoOjeG4eVF6S2K7Jjy1R5_oxp80TmDhfRsANO2X6frGGI5SsHvMC7s4SEzH7YTNp6EM81oSlHfpkRMB0v34Sh8Fg4VgdTeQcMInsaF3eUdbZgBWu4rno3xUS3VhGKgyQFPDWXn2hY08fkHAB2AFyahjDf5VURyzoB5QgRsx9g1ehcDFKbP_GX3FYn3rtX4I1WvEmrTCKKQ2X0h96BWs-4yXy9358E7K8vIBgc-rQw1vKkswmNFUN2EVGMFevHnIVIeAzyy9e9lzgC6xafx9wROhwFH9T6Vn8tSKd-8f5PyGWsIZfvsNQ_4wSQaNYYNH6yIM_BIcXXrp2ZkBG_BzyhYKD06kfXvQu8gnsK7ycUoVIcuYNE7oY34bAT0v2yN1xxQFX3u7jUG2NgyPTmUAyqApRz7dXVn255vXwd-9-Epcz0aMoDy0VDSCI76g_bYOmSIMW_RPLWs8lkc67R0k_UtexdvwOgiJc_qOSAElyEsurksw1xSRs68RHwBbun8KHIeHxCCwcla5xCiwr_O3A1djRh-3yCgrulwAcCocYzwGXUScevqEwjZ0QARGJYZGYyjOMF7TVb4h0F1LVvgxBx_BQoBusLJS_MtmPicxdwZaqItQt06hq_qXB7ZtWCqwB5gLG3iywgF68ImHgSaAR6iggPndmxp8Zh9egdh4M8eXT4oHqPhzV3zL7_jkcrhJXehI3DyJ4eJ23gFxJxosMU8QwhNy-g6GczRGR8EjQkav40O8EBUbsqRZ1QjbsjsA3srATu-8dx70gO_1o_o5jxTpSd81Ri4otRmBfmye4HIP34pRcHJKQzs0wQhCaouKY6TOvNLR3Pxm11qLHzc0gpXFjkKntLYRNUqvNmw_MIDfYUvcsAslrPFTyvnv0CN2BhbHn3s6Sgo1eQFPTW1JQuliST2THtRwqR4fgJ678AHeyM6N6Hi6kLpF4L4hMPYIUaLMkzlOp6_9EgBwaNAs-8scztw4f8mJ_XWMyA1rTksjaYl2ENPWdq7Y0gxRMjeGlIcIROl5edD4w2B0JbDyylRhxlL_S-7v8huHtSkcYXzLUIXeMT5HwnPxzE3J4gOMriLEPFyXlX8rHpYEmPjxztjOxg6nuXdetcKjOO61d8IQKItfPoMiKTKZTbcl2yr0zBZKXfY5zcg-sk_NReIKzOaig_nYFFG67lEfAxHxNshQiYXKrDd833_GJ36m8bSGVyJMlnuF7uv6Go53Jt7le0YbCth",
              "width": 300,
              "height": 300,
              "precision": 1
            },
            "place": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLngsfcpn9-qGNL1nqw-_hUG-iUbaXKNlQ7TOHXGC7Twh8qBagvJYCkHMF_fFPdskF0MUzLzg12Nx48mszbWPQAoMCH49IFdpkPUe4gsKn5SwHivl6i8jhDFmzL1xQT2dAGGjenCxS6hzT9SXpw0ZFffgVw1eMfXCYqPqPSxVvrJpDxktTCJUqfHXvXGYe3-l0C2JhVsdEQfg5z6_8WLujwMxQfuQcbq5Av-FBZa-uCVGwzb-3-NkIWIjW-9sBQ1BKG1I306Sl_pT5__yeejMxLPdCFeaTtPnwrVfzAKzrUySwXDIkRKYOUMcJIenH_m3pvDFry2BZkIx4WnOLKQtI4gPSh1dgOcqMyUdMppafMXiLFtmCU6C9cNlbV6Cgi1fEiMD2OJR6bhRr8SHVzzJxhdTBBwfEIQhocLJLGwWTpD4Pfr9boKFWbOGT1FJmB-HAo86lbntEubB5e5toHDvfyLQEikzAYurgw_UBQd92bV183RMnoKUMLETGh4fF85TCP3bHWxDtHvgRq4Qi6iuR-CfeZbb_MIUobWf3JHSro9AYXAZMwLaewA9x2R3bCuVxgGk3s2zplBD47nuzTa-4Duv2R5v8kQqwmRf44vrb3ZwTgsmqh8RpZDE7-6iss9skgBCC7CTSpsh3tQXJD4Zt-aQZQx-oERBwqIJDi33_HMqLtkdTgImG7J2ngCreJ_lYB2KVJnPM2Qh9w4MY8EuvqGTAZoRYaiqUF2mlVQcGhfl0BWefHHVMwPAqd789k0yeQ5ofA8ChkogJB3Sq6nPhzIN2dSq7VLFsfZcHCOxDf7yY1KK8qOaOUBex2U2fZpHBZDkv08jllFQ4JlNbJWskTufif7OIXY6QVSeI-pZ7PZzTbpGKO9hBwNlf1-Cg209MfIyqsNguIhBXtaHR1z4d3fzRD4tsVQAUIDb7rzE_UI7_jhuvwJ1yAImDcOJyn0Gkr_Z1CgvQVew9x3_4SLMrUFxEduSEQoooy8VZJQuKXWUwoaOftB0Y8LxW7_sJpzjuA0bPU4AlLnThHwwO5qc9vI9O_c7fVHn4vXuLjBTHG2CUnCYEqNKGTIeRMZG_wmkRpK37j2DtZKAIrsc7DS8Eist-e1usqU5olbuwGlK7eSxT1hXyq6CtKK1jc7yM23-8HMwGMJSmLgDzsc3xD5LNaRSpo1fIXWRcaDJDm7HnEN6P2mffAPm2dAGL9Fqih8lkryaFNsMojfy1y_NgFLczDMR0YsBUSgI8S_1N5ccK9Y1kIXsjTPlw3ITi4981G6w6E967LxwtUtDpl4CumlN52Hd-TXaPjEnkAffvBEyLz0hQGDJE1D4WwM9BhbFf4g2VfIU3E2QV3Hh8MmvD4fe8koeOE1ug7V6YBfsYUtInWcyDylW-e5DBgLUnU5yYE6c8MID-TAwuVjzvUVVFZ25JDYi9O4-k8ahgeAZvX41_LELz0tf3gJmmeNm32KZe1y1sM_rdLqvcXUz1rxuc9Kfb1PSE4sC4QhpIez25nWPmBR08OT_XfA34wFwGzw9lMyympx4f0xClOhR5-2w-hgsRJI_afV4PXC3gJTNT7ECfSxjQDJbsFEayCP9BcTGzct2R9CU7g7yt3OiE_teDZTOwIieOA6PwbYp8eUfwrpLbWeh3btFSQyS59MlHM7hIn2-YtFQK3Fx-ZrhL_V3FozodddDJN8dkFdhE0GL3x3nL-NaHzuNDDBnCvEU7zK6Oi93Aow6tfiNcMTBlT3sAUMPjxHx4fihQ9n5QOz29YT--Sf18RS-HHGHcQFx2f8-1q9AC534Ds-wJHlhRn4iW_t_VrAd6AQ43ICXgXVsDrFgHV5yQnLpYVBaqiFNttf1D_pERaGGfUziBDHQwIjsvuauUUhOW6z_ACU6E7Ut4npZH0aC3BmV6c7jl_Amjc4jca2NU3ASGKGR2tjDXgS3JxwK1bZhdN7s4rQT83KpHSzW7zFIbCocL_P2-8OFzsCLiQ0lkJ2oR3lPQ8XSFM_MsUKMTyJD4gig4VqZE67VxESceWUnw5aeHmCFwZIgO0z91_1TWqwpTc3Th2mDxY4C-Hr_lWF9q5WYfFMV4cbfTBNTvR0iYjHocpMpqgJNlfT1rarVhGB2bz8jZVNR87he_-e-oyg8Gb48kcSbYcUO46s4HoRz70p1S8ySF5OVrM7BU69esRIgK7Njm4iz7HWkhm-J5nYxNI9cEkWBkqOLjQzknsDr7_utf2BmuNEk3QH6WJ5HY53oFIvPcWTRF_weEDNPrLIxQfuy4ln6MRxnRHUvCGeHgle8vmOkUwFSOc1MlE7QSk_JLF9hVjmh5m1wewrORKH8GUT43BCkwgU8nEBQ3U8TIWCKkLEoGWPPNddkP8oG9hNVjszSNkATIate_JftQwo_Gh6eABQos7UuAAk5__SBTpnHyQ7ypRO23G2Bsl_cQ8GAqZCzeAtD3sS2RM77d6XxFGyOo_fiAvFaXB8VDTGLHguMjzDFOXEE3FFIis9Gob5pxwh9EUeQ5v0A",
              "width": 70,
              "height": 70,
              "precision": 1
            },
            "placeCover": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnhMeU6X41_ghG2yCytPJvFdfFeYSWOgc9V9j0NDTdyDgcLpMMJqasO_dzZWjium9iBUDxzS5DBjwOr_btRsMDjtCywd0kVb4lSdw7oYHeVR3mqWO8zDpVPEjC_h4H2vA2CwOzJiaqkTHlalVa7Z5eWCZozfsoYAofEKXC0VjuEaTBhsPkOku9Om_sCrS2znUh4LtJhfUNSz9ewcQ4DMnTHjYbrAYOqKwAxV9bcvOSUUkxc8jiC3swDBu39M5g8zi68Y7I-R5OtgVb-i-rluV5FNqYTa3LFHAJSP7MJSDc7zA0PooRMZW4PPxAWGHDhGNhNW3y-ihhJBU1tMv7f9UYnMSy69sKRKQDcfwPh7fUXhnclGOBxS9bCV3h2RY57OohFCOJOBmWoD3ETn9QxLBUeSRGzPonYxcSLq734Ez8Brr9sNHVLk-COEb_JIm05Hg-5J5Wp_gTfT1z6-8JAubTICQLgQsruYwfx0FOT9mlUlgZbM3yAmcGFRiE8OVE5Se77L3M5gl_mjR58yaXtMhrLMGiWLPkMHYhfcrrOTTHzi8CDoYQOKOoAMFqWGzZpWdFEV_sxBVmGTcTu93sYdY0neOSxtkEXY0_SsYGt4TzdCnTgHes1DRKMmTH_BIz2fMUERmRExuVrh78TEtN8Zx-SxNB3fMgUzoVMbLB8UrnCrz7ht3XClGZFnveFre27HIKxIFbsuY9dTtVwsQFEOTxOAoKrw03gpAD33V_dOuDUGgEWerbB1EaLzGGxvhqyhOr15D32gdBggJu7B2hovx4D92kc4_GMGA9cOPBPRPW1yITCrosM4WSN9pKekXlv3NBNVncxAF3Aio_gsnqef83nfKi9NM-R7wYWsUDuY7uRwjbs3uw0i9iCmT3xwQ79vQeOCOIGAmWtDvmc2xH5qNBaiVJ3domZRQJOKTz4m_WG7jipPD5A0KpBWrDGKCJ_Hc3_4RSjtQWWxVq6OE9G_r2GzMarjIPrK4i4XtecPO0WkArbsHkG1I5GRaX78lq4Am-24Po_BZMjx9y_CqVtuxZIOKedZHvM1UKbODPHyrP1xA2OoEPEruzLu1JaGTLv35DMn3U_jZ_KxQLsuzfbtU1oc-u1vYmTa0Qa84kuLTnejjlg1y-6h5SG0jX6SUl0uolAj6HMR6dtDfaa3xsxrBjaSFg3MEuUz89FZ7tyVj_GaHwtvHXDmKfFX7fDb-VzG4G4qZQr_oiXTda6NUBFMjILTc4rREpu68k9l1SdfqAWGIuTs_hK2EZMyyCz_9F3jCk0I3F_x9DoDpH-AyIqctbP8ucV7LHLGgbdd7DMwTb4RwxFaIWMK2gG-d4SWHboEVnEW_g0z5HIw0qhObsSdQLj_mz8d0Ydps-bd0YorTkazzZp0yU-D51E3Dj7jU25uY-KDiWORaYhgH6YG9S2ZZBdy5n5OcDSQAcDLno727kMpL_svzcP225GlnAD5Of7HYC4ZBfpMUdSQ5Yz-IXEtL1GRsotCsWg6sewFFuVfq7WmQzQv_cNUgiDwiUye540g2G17v89CtXqhpg1Tyhlsh5Jfq4TInjK34BSuDqPw771QUwHJM5Cq6lOvNYTEjxkFtOI2Pg7h58Bzkrps7vbeIlj92NwvIIV6o9QfUYporwSwnguGOuxy5KE3nexxQN6MsgNSeOIR-spTPTQVpv_YJVew9Oz-UjeBUJEq_17HzUC472mOX6GVCUL3zdCJ6yz1Yb0Ld8occpXjJz698LBvDVAgQMjDMxqrIQxHNRcsCBd301Uv_dCl80HDCE1upsyhaP97vg2BtjjCVJxSSmjvdSLOmyVbDJNUswaMLCIBr1ygcwAoktGqiDPdJIaEPcgE9IA0jr3y1AJCoLgd_GWcMuu_qg9ckjYIw0XfgenK38UjjenWCMyy9tMWvu3TkH5Ow3Nxe3MROJmDDgW05MwIxXTy1p0PkgYRsjFL3Q7GPDJbnYm9fWOkOIIl36OYeg828Ew55uvuQybBdaysYkLuz2MhU0kxE6qqosx0hxTcCbX0swZt3uFlkcGB2n_shs6wak_o7-8ydTmQR81jmyvtFoHeeaarLDDVM8VdTGGQD_xz8WCbIZMIu5OedKbHPNvHh4AXjp7R1KASMXncDHfv84rdKzxsIHcJ07e_86vYHFTCLJumK81jl9LUT96AcNxMsvMSyFIR2ruB3efW1v8aNzWipi9-gadiMQKLjU6XjMKqD-hsX_OECvPUfCBJy1-lYA8rR_gvMvdSF1-sIhEcT1GAUEoCwQvbYS_k9bcvG7b30CTfbGFUIrCDej4tpG6zS917ne2zxHojxN2Ae0p_pFCOW4VIXrOlAhSdzdNBb1wwQENYwkNbuPPMReWWXjnlhjN2DD7yRTJy4guvL5YcAtnOae5_IHR5gFed8Kh4vsUSn0nWCy7BljOkvX9Twl6O0kGS6yKymlpxXxUFdn0559YhVh3Pk2XDQ5NYTW50XnMYbHg-jiKX-2AlHNG56q_1w46LZ_l_gCUDFp2Pos",
              "width": 100,
              "height": 100,
              "precision": 1
            },
            "placeCoverXS": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnhMeX6X41_SxOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
              "width": 103,
              "height": 103,
              "precision": 1
            },
            "placeCoverM": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnhMCU6X4y_ixOgC2z8vwiC_qEQ4PVGFI1cs79HTnXzRgQB5sIN4C4GfBTaWbIpkJqN1P07QF1MB08k8LHQ9YRutSf0eEIRoQkf-w3i6j8cArlnkmp5h9qO2Xj3Tc52_ASAh6rOjikiSPTe1VQzoVOSSlZwNEfWCI3LafA_l3IEqXyr-D0P1akGHn-HbKRy24J851zj-0MSRNY-8IXEdnNIyIrpRImqIYyxGBQSe2edFoiS_bOJ0ULKR2vy-N5zRmaxrnF6x99qC1D3Rmar9JVP-Wie5LBGXU9Wt7kAC7k2R8bNKYBFr60GsB-alHOhGBDDEjJ-zhjKw8ok-jBbccLnOy_5cc-TI8gRdE3tqHpfj_wvW6h2ClwLHrD5ykG58EeIzqBMBGKgwLRVVRRwYZTRBdS9eALSjUpEZHSz0nMLafbvM7JPXypB33bApCc1VgL3rdYvuMjSS1K6-8aNMjtPCA1sC8Mn4Uj7H9VWeSCQkMhePLlA1MUKACcz_xu_DWr5LDM1z1QuhVY5wyEgPZTF9CWXI7VAlQibO7oASfSySMmHqYMDJ-wPuRMdG_zg11hKkff7CZgBw4Ps8XDY94ioNeF7PcNa6UQSsUjm7DybwTJm0ul0hxpGX_5_wIE5M89Gzi1LSSmqTDmUkVYxrZ-QwhOw_ENUTkvF6fezW3SNonmnfz3P3SjM13ED4WC-1AN-J5zsvEhazVk6sEcKPPxIDgBgRQ-uYcT8UpycOG0XnkIesT4LXwgODux9MBgwi2d86_34StkqTZE4Se4ovZFC92_doryE00vferUPSz08xQ9PoQlMIWkOsBKRG_nkkZ8Bn7L6j5JBA4eg_fJWcQTh8eG6fkHdpYxQvYvh7bpRzzJq3Cz2jNuE1bD5gkW59UYAQeSJzOZlhHQWkVxwIBQXwFY8eIoYCgrDoXz42TBBpr3gPLgAGSmDmbBBrmw0H4jx7RWivo_bBZd-sAjEN3PAQYPoBAmjo073n1ZT_23fU8va-3JLVY6LTei6-ZxzyCA77_A1T90iBl72yGmi_VwPMG8eKjLCk0dWNrvHg3K0g0KPZYEHoWpOMduTFXQmm9CMk7u3yljBjIjj9XsQc4Cj_aNzvg9f6sBfMYIiY7Ydy3li16SxBdwKGze6SAB7NUUPR-CDBOKtBLUc0RqyLZ7ayxi78kfSSoyHJfyzWnhMIrjnOf_HFS_P3vjBJie5HgB97RitvUNUiBZ2MMANsrOBxEprBUvuo8Z211XSs2EXWUVfs3_AmgDNzysxuV4wA-l2rvmyCBTigZS2QOFo-pNLdiCdITlHnsRX_XMBy_cwTgADLcBDpqSHOR8eHjYomdbE3jk7A5iOBwVkvLHf_U0ofCe8uI9fLoFQOIYo5z4UCXdv1mC1yN8M0bY-CgJ6eciHRSRMgyslgzbdHxM5axESjVF6u8pUgEBE5P_xljuFoXEg-XTFnSnO3jVC5Oh22w49ZNVoPMXbxR1yNo6CfLKPSclkDUvgY0fxlFnd9OtZlkxaMvuP2Q-FTua_-5M1AWF_ZbW4R9QqBxj_Ri-h-1bN-e8XYjvPk8IXvz9KBXfxBkULLIoJKqMNdZweEX4mUNvElrM7ypUFhwxrMHob9QFoty28uYDaJowef03maPobyXUgnCj7C1RLVvH4DAA3cQQNDWkDyi4ggD6XVdOxZ1RXytT9-w7YjgdGrnm4H7TO7DhnuLeO1eHIknyKJaj73sE3rdovOc1Tw9q7OIiLtvTMyMHrxIVu6AGwEFnduy6cEoJeNTqK3wlHBua48J84CO61IbO5gdvgxVw9wGHrfNuBsWedZf7MFAKXuLnPAXZ4h41PJYjCbqYM_Zbc3TLpWB8Mn3dxh51HSgWgfbTROMjq8C79NwkZIMBR9g0u6_pSAfGsmqO5iF2Oln32SAM-PkTBy-wLBW2gDTYekhSxoRfdS1B0uwkdRYqNLrUzF3AJ73AudPHKWu-PVrbOomA9Ekh95Zxk88pbD971P0AJdvLDyA8jy0VoYgwxXVFRfC8WE4kW_zIK101NxKv_elA0Dab4ZXT8jdJuSR-3z6Fp8t2CviIca7hOl0yeOncCC_62BoAPpITGIavA_RrcUb7r0V1LmHCxzlJCz4-ksXYYPMypOa80P0IXZ0bUP82i7L_WBvpoV-w7AFRIl_M6zAC2tk-OQmTDySZpCHfcW9D_JNnRhFE1uk_ehkzEqfG5V_DAKLage7cPGKHOWvxK7WX6VAX2KZ1lvABbxVr5M49D8zXMRk7pRIkgbgG915ubfOnb14OX-DaAV0HLjuY3cFbxA2j0Jvt9C5ilDF8_QCyj_x1F-SAaoP3MFkJatXiNSrK7h8jKqcFNqSPGMJzW0TCtmN4GUbw-SZ2Hg8Kv-ToYMQ3muSc4McCdIAQbdg0hYjfRgzmi0KLxC13KXfO3Do21MY2FiSpBwakqhngckRS0Llwbwx41OcCUQIVK6Lr-E78GZ3MjvHeI2eNAXHzK6CcxHUHxIRNi8g6SRdf-94s",
              "width": 170,
              "height": 170,
              "precision": 1
            },
            "touchPlace": {
              "url": "https://afisha.yandex.ru/267GrD541/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnjcfcqX9aoDhG1zy-tuZ5WtKTLoefPnEtRcjaEivzzjYiAbkJMaKjPM1xVk_wunNnNGzk-DtXBSIIsMnOSsAEjdC7z8E_d68_XcQJkozuSDbIq3SHzT9uN0_i6RUT_dkbAiu5BQyosSX9Q1lrwYBQTwha4ts3dBsoPIzX41jqFbnSgtHfPGiJD2zRPoKs0k4k4pJNsNM8eDR1xOIGMNXkAx0LkQcxmZEQ82tHZ86RR1QNQ8HADWcQOgqT7_5x9CWx2Z_12jdXvRlJzh6poOd0B-a6c6noCm4LfdnOEwz75iY7HK46JaWoD_B4d3H8uUNKN1vi2hl-Pjk1pvDYUdIQjfq94dAlUZcfaeI_mIfqcgvIln2Swwp7FGjq1yMJ6sY7ODWGOT2kkAHXSXBFy6FSYQlb7dgqeSUjCb3D8U_0KY_As8XbA2qgHELsPKihzUoB_bBAruU-VR5e9ewpMOv2EzAGtBYRhpMO5lZtUM2Ab0sIU8jcO34TCQ64y-hu9TiC3YDi6xtmnxBA8jyEst9vPfOkXI3uIls_WsXaCC3k0BY3HacMNZmVJfB1bVD4nWd4KWXf3SRcGDYjse7bfdM3rde_78kMbawlYNIMv63afR_cu2yJ0jFCMk3u3RYQ38MBIB6EOjOHqAPjVEVp4ZNlZhhS6ugHfjo_P6zF6kPyL7nMseHFGESdPXDSPqCr-Woe8KVegO04czd1-f4rEvPYEh4AqC0Nmos6121fds-wcn4ves3qJ0Q6Czil5cda5QOv5rzs1QNQiA97xCqwofxzO9iYfo34PlYWcMH9GTTpwRILIawqD66OBdJcUUrsmUN-GWXLzD9BNA83t_byftMmneW11dM9SrwmZdwGop77dSzQp2qS-glCAnb41TkX1eo7ORWWOSmisjzEXlJW3rJTbhh77N4pYjMpDb_g21L2Npvhn-jWKFeMIH7FAbCuxFEb-Zlsq8MWTB1QwfU1FdDhAh8_kAMzu7U09mlHQcWYXUkERdHpBHIdGhGU5e1A8A-8-Zr92A5NlB9M8D6ggNNMAd6GV47NCUoVfuPEADTb5CIwAo0ULre5BsB9f0rhm0RaEV_8xBZ_AD8SguHYfO8bkceQzdksQo0tQt08q6PLSxz3qVKjyhhuIljZyx0J7tAmNjyBMimujiTUdXJF_LFXRxlg5OgCVh4TE5TX8lDvJIngseX2HkeYPGvaHYC39Uw5-7hCn8U0fB1k_foHK-blIBwcthQyvaIS-mxOdce6WGkKQOHaJFgnDzGiytN56gSy1Jn01yFooRtq7SGHgsxlA_ylf5HwGFMrcs_qFALX4w0TG68CPYKzN-F4b1Xav2dIJXL0_B5mIQkYscbZQsEtjOC78-IabIs-fsc8qLLPdzjng0CD7RBWFl_J2CkF9fogJzSJNxuYri_HS21j3q9YQCFGyfI9dwc0FrLh6XvcK43tutT5OEi_I2n2F6Cv8U8P9LN9oNENfjpT6_wdFtLJMAUmiSw2h5QexkxOTsW8RWU6ff_zH2QDGTez999EyAOE7ZLAwytIhjZaxB6EoNZUJ-eeW5bmAmwVW8PgNDbO4gQiNJUBOKOnF-RRRWXEllVEJU_UxzpSICswsuLvbMEJstOU48Mrb6cWfsMCvJL6TifIuX-T0hBfK3bo4yco6-c_PyyAAziqhw7ydkl3yqN5aQpE6cMoYhkiC7Hz2ULAIqf0nPLEFX2aPm77OoOP6H4o17Z_lMYxVR5u9-g_NsnWFD0-rgUviZA8-Wt0dOilQ3U6fMDkCXc7CSi348dfwSOE8b7w9w13ryZCwwa7i99HLf6ncYjTM043c9z0OinM4ho4IIUHHqSGB8BaaHXQkHVvLn7n-xlBAAwhm9bOZ_Uun-SvyPQNZrsbePklsIvLcALLm3OS9TJNG2zF6SsP_OUPBjyMJgWptBTmVXR5yJdbThVY6tomSB8wLrHszmz3DKTGsNHXCXC7GV_iKL-2920Bxalcj_QUfD932MAjFfnHLCIcpQU3tZMH2VR0bsCTRkEYT9ziIXMWKgCV4-ZP6iqx75XMxxhWmjVf1zadse5JBcGle7DLP3Mhd-XuMCT0xBEDFK8kJKCzBcRqeUnnoHdfLEzX8TxIHBA-mvHyceMGjNek7OQcaZ0cXNgJiZXRZyXJq26E5S5iCFn74wso5OM0NCyCBCWEijLFdkVW7IJcRTJJ0M0eeyM1KrT3wWPuKrnUmdPULm-hIWL5PbaP81wr1JVLku0iUw9z3f8LFtPXHBEhjxIri6oA82tFTvCldGozZ9_5FmM8LhyHyeZ98wOGz73X0yNuqzth0S-2nPtLJ_-SU4fIIm8pbMj4OiDP1i09KaoUEqWQEfF8V2vHu0FHBk7u6BpFKzcMpO7NZNIyofaU7NMZV588bOIDoIjaWgLLpVSk-zltIkTAyycO78s2Aya2CjqMpR__fmdr4rpjRhlY_OcJUj4JKLrK6njIE7z5hMLrN1C3Ln37IrOFy0Yp1IBAv8gyTy1L0A",
              "width": 80,
              "height": 80,
              "precision": 1
            },
            "touchPlaceCard": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnhMOU6X4x_ghG2yCytPJvFdfFeYSWOgc9V9j0NDTdyDgcLpMMJqasO_dzZWjium9iBUDxzS5DBjwOr_btRsMDjtCywd0kVb4lSdw7oYHeVR3mqWO8zDpVPEjC_h4H2vA2CwOzJiaqkTHlalVa7Z5eWCZozfsoYAofEKXC0VjuEaTBhsPkOku9Om_sCrS2znUh4LtJhfUNSz9ewcQ4DMnTHjYbrAYOqKwAxV9bcvOSUUkxc8jiC3swDBu39M5g8zi68Y7I-R5OtgVb-i-rluV5FNqYTa3LFHAJSP7MJSDc7zA0PooRMZW4PPxAWGHDhGNhNW3y-ihhJBU1tMv7f9UYnMSy69sKRKQDcfwPh7fUXhnclGOBxS9bCV3h2RY57OohFCOJOBmWoD3ETn9QxLBUeSRGzPonYxcSLq734Ez8Brr9sNHVLk-COEb_JIm05Hg-5J5Wp_gTfT1z6-8JAubTICQLgQsruYwfx0FOT9mlUlgZbM3yAmcGFRiE8OVE5Se77L3M5gl_mjR58yaXtMhrLMGiWLPkMHYhfcrrOTTHzi8CDoYQOKOoAMFqWGzZpWdFEV_sxBVmGTcTu93sYdY0neOSxtkEXY0_SsYGt4TzdCnTgHes1DRKMmTH_BIz2fMUERmRExuVrh78TEtN8Zx-SxNB3fMgUzoVMbLB8UrnCrz7ht3XClGZFnveFre27HIKxIFbsuY9dTtVwsQFEOTxOAoKrw03gpAD33V_dOuDUGgEWerbB1EaLzGGxvhqyhOr15D32gdBggJu7B2hovx4D92kc4_GMGA9cOPBPRPW1yITCrosM4WSN9pKekXlv3NBNVncxAF3Aio_gsnqef83nfKi9NM-R7wYWsUDuY7uRwjbs3uw0i9iCmT3xwQ79vQeOCOIGAmWtDvmc2xH5qNBaiVJ3domZRQJOKTz4m_WG7jipPD5A0KpBWrDGKCJ_Hc3_4RSjtQWWxVq6OE9G_r2GzMarjIPrK4i4XtecPO0WkArbsHkG1I5GRaX78lq4Am-24Po_BZMjx9y_CqVtuxZIOKedZHvM1UKbODPHyrP1xA2OoEPEruzLu1JaGTLv35DMn3U_jZ_KxQLsuzfbtU1oc-u1vYmTa0Qa84kuLTnejjlg1y-6h5SG0jX6SUl0uolAj6HMR6dtDfaa3xsxrBjaSFg3MEuUz89FZ7tyVj_GaHwtvHXDmKfFX7fDb-VzG4G4qZQr_oiXTda6NUBFMjILTc4rREpu68k9l1SdfqAWGIuTs_hK2EZMyyCz_9F3jCk0I3F_x9DoDpH-AyIqctbP8ucV7LHLGgbdd7DMwTb4RwxFaIWMK2gG-d4SWHboEVnEW_g0z5HIw0qhObsSdQLj_mz8d0Ydps-bd0YorTkazzZp0yU-D51E3Dj7jU25uY-KDiWORaYhgH6YG9S2ZZBdy5n5OcDSQAcDLno727kMpL_svzcP225GlnAD5Of7HYC4ZBfpMUdSQ5Yz-IXEtL1GRsotCsWg6sewFFuVfq7WmQzQv_cNUgiDwiUye540g2G17v89CtXqhpg1Tyhlsh5Jfq4TInjK34BSuDqPw771QUwHJM5Cq6lOvNYTEjxkFtOI2Pg7h58Bzkrps7vbeIlj92NwvIIV6o9QfUYporwSwnguGOuxy5KE3nexxQN6MsgNSeOIR-spTPTQVpv_YJVew9Oz-UjeBUJEq_17HzUC472mOX6GVCUL3zdCJ6yz1Yb0Ld8occpXjJz698LBvDVAgQMjDMxqrIQxHNRcsCBd301Uv_dCl80HDCE1upsyhaP97vg2BtjjCVJxSSmjvdSLOmyVbDJNUswaMLCIBr1ygcwAoktGqiDPdJIaEPcgE9IA0jr3y1AJCoLgd_GWcMuu_qg9ckjYIw0XfgenK38UjjenWCMyy9tMWvu3TkH5Ow3Nxe3MROJmDDgW05MwIxXTy1p0PkgYRsjFL3Q7GPDJbnYm9fWOkOIIl36OYeg828Ew55uvuQybBdaysYkLuz2MhU0kxE6qqosx0hxTcCbX0swZt3uFlkcGB2n_shs6wak_o7-8ydTmQR81jmyvtFoHeeaarLDDVM8VdTGGQD_xz8WCbIZMIu5OedKbHPNvHh4AXjp7R1KASMXncDHfv84rdKzxsIHcJ07e_86vYHFTCLJumK81jl9LUT96AcNxMsvMSyFIR2ruB3efW1v8aNzWipi9-gadiMQKLjU6XjMKqD-hsX_OECvPUfCBJy1-lYA8rR_gvMvdSF1-sIhEcT1GAUEoCwQvbYS_k9bcvG7b30CTfbGFUIrCDej4tpG6zS917ne2zxHojxN2Ae0p_pFCOW4VIXrOlAhSdzdNBb1wwQENYwkNbuPPMReWWXjnlhjN2DD7yRTJy4guvL5YcAtnOae5_IHR5gFed8Kh4vsUSn0nWCy7BljOkvX9Twl6O0kGS6yKymlpxXxUFdn0559YhVh3Pk2XDQ5NYTW50XnMYbHg-jiKX-2AlHNG56q_1w46LZ_l_gCUDFp2Pos",
              "width": 140,
              "height": 140,
              "precision": 1
            },
            "touchPlaceCover": {
              "url": "https://afisha.yandex.ru/267GrD745/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnh8WU6X03_ghG2yCytPJvFdfFeYSWOgc9V9j0NDTdyDgcLpMMJqasO_dzZWjium9iBUDxzS5DBjwOr_btRsMDjtCywd0kVb4lSdw7oYHeVR3mqWO8zDpVPEjC_h4H2vA2CwOzJiaqkTHlalVa7Z5eWCZozfsoYAofEKXC0VjuEaTBhsPkOku9Om_sCrS2znUh4LtJhfUNSz9ewcQ4DMnTHjYbrAYOqKwAxV9bcvOSUUkxc8jiC3swDBu39M5g8zi68Y7I-R5OtgVb-i-rluV5FNqYTa3LFHAJSP7MJSDc7zA0PooRMZW4PPxAWGHDhGNhNW3y-ihhJBU1tMv7f9UYnMSy69sKRKQDcfwPh7fUXhnclGOBxS9bCV3h2RY57OohFCOJOBmWoD3ETn9QxLBUeSRGzPonYxcSLq734Ez8Brr9sNHVLk-COEb_JIm05Hg-5J5Wp_gTfT1z6-8JAubTICQLgQsruYwfx0FOT9mlUlgZbM3yAmcGFRiE8OVE5Se77L3M5gl_mjR58yaXtMhrLMGiWLPkMHYhfcrrOTTHzi8CDoYQOKOoAMFqWGzZpWdFEV_sxBVmGTcTu93sYdY0neOSxtkEXY0_SsYGt4TzdCnTgHes1DRKMmTH_BIz2fMUERmRExuVrh78TEtN8Zx-SxNB3fMgUzoVMbLB8UrnCrz7ht3XClGZFnveFre27HIKxIFbsuY9dTtVwsQFEOTxOAoKrw03gpAD33V_dOuDUGgEWerbB1EaLzGGxvhqyhOr15D32gdBggJu7B2hovx4D92kc4_GMGA9cOPBPRPW1yITCrosM4WSN9pKekXlv3NBNVncxAF3Aio_gsnqef83nfKi9NM-R7wYWsUDuY7uRwjbs3uw0i9iCmT3xwQ79vQeOCOIGAmWtDvmc2xH5qNBaiVJ3domZRQJOKTz4m_WG7jipPD5A0KpBWrDGKCJ_Hc3_4RSjtQWWxVq6OE9G_r2GzMarjIPrK4i4XtecPO0WkArbsHkG1I5GRaX78lq4Am-24Po_BZMjx9y_CqVtuxZIOKedZHvM1UKbODPHyrP1xA2OoEPEruzLu1JaGTLv35DMn3U_jZ_KxQLsuzfbtU1oc-u1vYmTa0Qa84kuLTnejjlg1y-6h5SG0jX6SUl0uolAj6HMR6dtDfaa3xsxrBjaSFg3MEuUz89FZ7tyVj_GaHwtvHXDmKfFX7fDb-VzG4G4qZQr_oiXTda6NUBFMjILTc4rREpu68k9l1SdfqAWGIuTs_hK2EZMyyCz_9F3jCk0I3F_x9DoDpH-AyIqctbP8ucV7LHLGgbdd7DMwTb4RwxFaIWMK2gG-d4SWHboEVnEW_g0z5HIw0qhObsSdQLj_mz8d0Ydps-bd0YorTkazzZp0yU-D51E3Dj7jU25uY-KDiWORaYhgH6YG9S2ZZBdy5n5OcDSQAcDLno727kMpL_svzcP225GlnAD5Of7HYC4ZBfpMUdSQ5Yz-IXEtL1GRsotCsWg6sewFFuVfq7WmQzQv_cNUgiDwiUye540g2G17v89CtXqhpg1Tyhlsh5Jfq4TInjK34BSuDqPw771QUwHJM5Cq6lOvNYTEjxkFtOI2Pg7h58Bzkrps7vbeIlj92NwvIIV6o9QfUYporwSwnguGOuxy5KE3nexxQN6MsgNSeOIR-spTPTQVpv_YJVew9Oz-UjeBUJEq_17HzUC472mOX6GVCUL3zdCJ6yz1Yb0Ld8occpXjJz698LBvDVAgQMjDMxqrIQxHNRcsCBd301Uv_dCl80HDCE1upsyhaP97vg2BtjjCVJxSSmjvdSLOmyVbDJNUswaMLCIBr1ygcwAoktGqiDPdJIaEPcgE9IA0jr3y1AJCoLgd_GWcMuu_qg9ckjYIw0XfgenK38UjjenWCMyy9tMWvu3TkH5Ow3Nxe3MROJmDDgW05MwIxXTy1p0PkgYRsjFL3Q7GPDJbnYm9fWOkOIIl36OYeg828Ew55uvuQybBdaysYkLuz2MhU0kxE6qqosx0hxTcCbX0swZt3uFlkcGB2n_shs6wak_o7-8ydTmQR81jmyvtFoHeeaarLDDVM8VdTGGQD_xz8WCbIZMIu5OedKbHPNvHh4AXjp7R1KASMXncDHfv84rdKzxsIHcJ07e_86vYHFTCLJumK81jl9LUT96AcNxMsvMSyFIR2ruB3efW1v8aNzWipi9-gadiMQKLjU6XjMKqD-hsX_OECvPUfCBJy1-lYA8rR_gvMvdSF1-sIhEcT1GAUEoCwQvbYS_k9bcvG7b30CTfbGFUIrCDej4tpG6zS917ne2zxHojxN2Ae0p_pFCOW4VIXrOlAhSdzdNBb1wwQENYwkNbuPPMReWWXjnlhjN2DD7yRTJy4guvL5YcAtnOae5_IHR5gFed8Kh4vsUSn0nWCy7BljOkvX9Twl6O0kGS6yKymlpxXxUFdn0559YhVh3Pk2XDQ5NYTW50XnMYbHg-jiKX-2AlHNG56q_1w46LZ_l_gCUDFp2Pos",
              "width": 220,
              "height": 220,
              "precision": 1
            },
            "touchConcertPlace": {
              "url": "https://afisha.yandex.ru/267GrD643/f4cb4a4aFif/RMQiqQORjMvOKTUpUXiEubMlsr1Kn3gOU3AYbaj6TIP15hpjsM1Xy8zn5xlcayPbRB4onc9jPhOpQwPRrntdzhRHJO6WwJrbDjvw7MYtVLnxs-c6Xc9tTEc1yzlp6B6JcSof5HhM1c2f_3hKwrz7Tc4FYsrM5auE_9te2H6gXFaGXvD5SpSFD4cs-vgePYTqd2C1NYMT70AcM0Uv6fyezreolWi5gtZIVLdyysGzuclISW5JBenlDDXUU1n2Y1SRBNP__sHQD4vKLHS_mb1DI_ts8HhHG-BBmLnLYaQ7Hgs3ZhzqfUocRxKwusDBPPWBRQrkTobqIUnzFRURMK3QU8BeeDDGmkgHyC6z9pj_jO7-5bewTdjtDxB4wW4iddOOuKQboXgFF8eb-T8PDnn6jwLKIIKDZqtI9JuTGfYo1hhAkbV3DxJBiocme3Oaew1kf228uAGRLk6Tc0ptrL8Ti_9hV2c0BFOPnLn1RQ6_-sEBQ-zDTmttTL5UExo2pBfehh6zu8VVyATHqPj6mLKDqb-nfzjNmKeAkf4D4uO2noB97NCp9ooTw5a7-YmFdPJBwo-rBAsq5QP01FETd6BWEwyfcvnDHYhAhO-0M1S0gKZ8p_i4xpxjCd79huXrdFmD9a3cpH7NUAoX-j9NQ_31gEhKI8QLJ6JB-BwclrfnnpHDVDCwj9lBw08tO_AcMUJqse_wtMhbok1WdkEp6ntdRbboFmW5Qh7O0j__hY58cg8BzuuOBWHhwX-QUVv6r1YZQRM3-kOWyYVKK_hznzRIJvfr8LhPmiqIlj1GpWg0nwn3phOtdgKVyBbweA6Ls_VHz4PlyIKqaQS5nZtSOidYmUwS9bJI0IxOT6F7MNsyjSO7aTU9S5irzt93Se1rcd6Av-ddrbqLE05W9TBPinN4RoBCqYsNoqNI-ZAck7OhWdrNETE2hZmBxwMhuX6avQuusS6zNk8Xag9atUYobLFTRbrm0-eyg9xEnLm9QQ66-0mOBykLyq4pjP2QWxp3JNEbBJ-zMw_SiIMCoLPx2_hM4rCodXeLm2XGV38JqeL_FIY9L12vsYNdBlLwN8CAPH0ITAukzo9o4w90V1SVOu-VEIhYufJCVgkNS2aytJhxymS_ZPg4T5DgARH2zmcrvJNHvyTVI_zLH8ca-_iHxfs-C0CGIcCNoePJMJISHnGrFlfBGHxzTxkOyEApMDiYOUmi8-dzeM1YJgDWvIWmYP1XDrLtW6A7hFKKG_p3BMx6-EaIAyPDzmapTffQHdh6rhwQShg5_sWSDseGIPhyk_XI57etMrCHnSmBH_-B4m_-nAo9IlKsfQzQh1pw_wkF_DyNhYiljMJoa448VNXZNiefng0QtHmN2E-PiO3ydtu6Ayn-bX9_hlBny1F-Rq0sc9cB8KfeKHnGnMbRMz7PQH_zSczOYISKbyrB9B8ZXH-pEB-MmvC6j1aFRcdg-vcW9MIjdyh1-M2cZw_fuI8i6PSVAL_sn6T2h1RAmn41Bs02dc6Kx-xEB-4uzjYeFFM8IdRWA9lwc0NYwgRHI7q-0DxLLnBtubIPmyiB0nxDLaA7kkq075ct-4OdjF52sYbL_TIABoetjMyo6gl_WNqevGlQlwiRMDbO1wcORWOwu964iyA1IXUwRpjhRxh4iGQttlGOPy2dKvHLmoaTf3UBwL67DMTPKs4GaKCNdx8WFHFgHR_EEPBzgt0FTMjsMTMeuILofSh090iUakGYc0GtLPtVAvCm1-o1DBPH3bgzBIA-uUTCiqMNAustxnxU1NswZJERhl4wt89WhQYNpfM3X3cGZzcsevlHUy7Nm7SCbS0-XUB94NAo8wubS5d4t48Bu3GBDghkQkIjrEj7WNrReazUWQyW8TPI0cVGRWS7t9OxBOpxJ3T2SVIjA9r-xi6qOx3Gt6ea7_JMWgaU-fAFwTc6xIDGKAVCbaEFfd3aWL5o2dfN1Lo-ip_IRQOh__nTcQCvfmn6fouSJg4RM4kuLLKdhnygXKi2BdYHUbZ3B4lx-YgED6vCQWugzvWTE9v2JxuQAtdwsAqdCM2NaXg_m7AFL37gPL3IXWkJUfAFpevy1Ao1ppvi9ANXT9l_fw3BvX6BwMBrgkSpocm2UFYWeCbVUkRc-bPAlc-ECCMxeN-0TKc14DH6QNyvQFDxBqwkPR7J8iaUqXDPFA8WNz0PSfm7ycBHJAENYG0F8d1W1Lzhm5DK03p3RZpNzwdtPTDXdUNm_6DyNYXVoIvY8wUpaTaajbhtEyo-DBAG33rzBAH58seNh2MOCqKljzda15Vz6RdfA5Zx9slezoQKLfJ_G3nC6fDveniKEygFG3RKoCy0mYH5p5qtPgOdy9VzsEdEenEPgQrkTgylrEU8mpwWvusRWMVb_TlAmUnORes7fhq6gqt2b7B8ChfqANh-i2Yp_dmO8CBf7PJOGsuZOLJOBfQ6gQVKYYqF6GvId9fWWvqoGN0DH_Xwil8BggwlcTDatAzmd6z8tw-S4kSRM4an4TEfTnLqXeA1BZLM3_cxiQJ-MMxGyeEGheErgPeQE955bN0YTJbyeYOYBwpLZrU7VL-NLHMouv9LUaYDm_RP4uf93YbxKZ3jMModRtK3tA",
              "width": 88,
              "height": 88,
              "precision": 1
            }
          },
          "address": "Тверской бул., 23",
          "type": {
            "id": "5575d419cc1c724f5a8e1151",
            "rubricUrl": "/moscow/theater_place",
            "code": "theater_place",
            "type": "place",
            "status": "approved",
            "name": "театр",
            "namePlural": "театры",
            "nameAcc": "в театр",
            "nameGen": null,
            "nameAdj": null,
            "plural": null,
            "rubricPlacesUrl": "/moscow/theater_place/places"
          },
          "tags": [
            {
              "id": "5575d419cc1c724f5a8e1151",
              "rubricUrl": "/moscow/theater_place",
              "code": "theater_place",
              "type": "place",
              "status": "approved",
              "name": "театр",
              "namePlural": "театры",
              "nameAcc": "в театр",
              "nameGen": null,
              "nameAdj": null,
              "plural": null,
              "rubricPlacesUrl": "/moscow/theater_place/places"
            }
          ],
          "systemTags": [
            {
              "code": "theater_place"
            },
            {
              "code": "theatre-go-place"
            }
          ],
          "city": {
            "id": "moscow",
            "name": "Москва",
            "geoid": 213,
            "timezone": "Europe/Moscow"
          },
          "metro": [
            {
              "name": "Тверская",
              "colors": [
                "#0a6f20"
              ]
            },
            {
              "name": "Пушкинская",
              "colors": [
                "#92007b"
              ]
            },
            {
              "name": "Чеховская",
              "colors": [
                "#a2a5b4"
              ]
            }
          ],
          "coordinates": {
            "longitude": 37.60150099999997,
            "latitude": 55.762302999999946
          },
          "bgColor": "#8c3130",
          "logoColor": "#d94c4a",
          "distance": null,
          "isFavorite": false
        },
        "placePreview": "Театр им. Пушкина",
        "placesTotal": 1,
        "preview": {
          "type": "months",
          "text": "Ноябрь, декабрь, январь",
          "singleDate": null,
          "regularity": null
        },
        "collapsedText": null,
        "regularity": {
          "singleShowtime": null,
          "isRegular": false,
          "daily": [],
          "weekly": []
        }
      },
      "distance": null,
      "isPersonal": false,
      "commentsCount": 13
    }
  ],
  "paging": {
    "limit": 2,
    "offset": 1,
    "total": 2853
  }
}
"""