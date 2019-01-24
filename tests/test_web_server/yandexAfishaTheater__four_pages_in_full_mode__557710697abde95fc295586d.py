status = 200
mimetype = 'application/json; charset=utf-8'
resp = """
{
  "schedule": {
    "params": {
      "date": "2018-11-11",
      "period": 180
    },
    "collapsed": null,
    "items": [
      {
        "date": "2118-11-11",
        "sessions": [
          {
            "place": {
              "id": "5516a4171f7d154a12dc66a1",
              "url": "/moscow/theatre/places/mdm-5516a4171f7d154a12dc66a1",
              "title": "МДМ",
              "logo": {
                "bgColor": "#4d4d4d",
                "microdata": {
                  "url": "https://afisha.yandex.ru/q2a568P13/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-oci_iQdWgeMEeWKYYOmgh8r0CcW0z2sg2bJFX3ut3gV2-zMPkqZ8RaBhc6AxNOb3-rY2MAHPaKyoXoIMbbMvkoP2h6E_RMK4ZVIF5F_Uh4n8_hHAusJeHfa6R1ZfjfgdftsAI6GGU0aMQ0eUOzHj8-WgOQkFy1mKjlGjIkeKFqGE8ruMDlXEon1PBf1Hxoyiy-EM1arRZQLWqWJ-b4LeAFzzMQioqXl8qEZhlD0n2sDOpwYHC-B2r750kzZzpTKHjeC3uxhYwbJ-bgLDXPKKrfndEfaB6kIa1plNUUmm0CJh_jsBgKl4boJYeowfM83XwIcMAgHZTo-wcZYqaIcPobfDhp0ITfW7eVg152L1mK761Q_Hkd1bOdaSZ3F-tfMTYegOFoiJelaGXGqHHSHc8NiqFAIh6lmrk3OOC3CHNZOG7rOFCE7Qm3hJHetS75m0zf8a3LP_ZivvrEteZbDdE1_rBBCfkFxvjlF3pTgQ_u_CkjcFN_xbhrN6qStfpTG6tPyDpzVbwoBybhTsbsGVtvvEL_e84nMg_LlQQ1Kx0zBp6BMPvqtiUrx0d7Q2HODlzZIzPRD1b460fLICd4czpa_VjKIrZ8iWYmo70GX2oIbK2ybagsBhFcCtT2xGhvA-VekPPYqWRE2Hcn-oETT83sW3MwML4n2uq1KgA0WmD5WXw5iMG1PHr0ZsOcBK6Lej6dEQ6ZziRgvFv0NIUIT0MXHWDyK_klFHsktRiiMDwPPYuRoHIt5MiL5KjChsjgWrrd--ihR2y7VVXDrdSc-vn-fjCfuRxmIn_qRqf12Q8ClR2DsKsrJdUKdbW5AnJ_7dxrAnPyDTUrGnYpcUTa0Wtbrqkpo7U8m9Q2IO91LTuYbp1CDYtPFvHMuaY0tmmvsWQcYRAYisTHu8fXuPAAz8wN-dMx0G9m6wlUK2C1ekGLaf76KrKmDTnklWDspi6Imj0OM20Z3_Zzj9uGVOY6fQC1vYGQ6Ng01VimR3oy8sweb7hSUfJ_Vuqq5Lpy11ijKZoN-znj9n-qh0bBXOWcCEpNzFEsW081ES-4ZHfE6Q9ypX-QgEq6ZNRYVaXKwNE8bf3KIjOw3ZaLmVV4g0VLUQq6jOkrk2W8O4fFIwxGPChK3K2ADmvtJuCc-bQ2pqhdsvWNYIJ5W3QHWgWFeIIyDh5MmmGTovyFCwlk23M2-INKmewJC0BETzqHpNP-5c4p29xfww_qTvSBTrsmNfQKHzNGLZNQ-KpENJqn5lhgw49v_YhwIxHslLhoJOtgxxkgmTm8yHui146LFGWyDNQMu1ot7dNuq46E4L7IVMX3KH-h1B1AMztapFfrB0eKcnLt3R_ZcnCzfreo-jTbUZbY0MpaDUmIMLcfq3YFsC1nnLvIP55Qrxm-B9Otiuc1JPqf8edcgnEZOPfnaFfl2tIzvfxOagCjcM8Xmah12HOlaMDYKdzLedC3rgjVJwIeJd5qKU-dcy6ZbmTAX8iWVPTIfkNGPtKSKRgEhsgmlApg8b7eT4pjUEPu5KtYNoozh0hSK0msulhShg5KhHfjHwR_WXg-_6N_Oq7X4b2Ip4f0Cn9jRA9xU2lpRpVIlEY4sZPOXd-ZY6MCj5Rb2FT7UtUIIPv5_jkqceffaKY1kw4k_XoYb00DXlk_F8Bc-PZVlhk_QXcvQKNICXQ2W0a2SIMTje59KJNTkAzGmdknOoOHyLB4ij05GBCk3AtkhYAMtKx4qu8MQl3JTUYD7siGh5foLpCXb1IhGsjW1PtGVEjT0i5_HfuyEDEt12lZ1wlhdhlSiyntCjmzJR07xYaRvTcfSUudv5KPag6EsT-ZtpVl6U7gB65zgMtJFKV69EfKMnE-DD7aUWOQLuTbGRcrk5Z4sgkJbwvqM6duSgQFs8z1P-vY7mwS_7iO1mHuO1U2lPqu81c_c7LZKGfVqeX1WnLR_Jz8mYFzk92l67t3-0ME-5MqOIy6KrLn_Gt1dCP-xOzL-p1NE15bDIcADqnVRreZfzHkbwDCKThmRPqnRRkhAf5_fftQcEKtJep7VTizdlhTKYhv2Tijt3_JFdSwLdYfSitenaN9mx018F66hYaHqq3Qhhxg4Xr6JibYFqd4swBujaxZkjHR3db6iKXY8cTrU3v4zNtKMIbOe-RUo1_GfPt57u3Qr2ucF4Fs26ZU9QmvQJffMMFLG3TG2iZFuzGw_I4_G3EiIm01ixi3eHOH-NJYGp_be7K2z6l2h1Fe5R3r6jyvQp_YLASCfInklXWIz5PWLvCweUjF1xqEtgkjIZ3ezQtjoqHfdUj4VPlBBqlDSFhNC0gi5T3KJqczndZuWmlOzjD9Ww03g02I9wb22h0gFj7TAvrqNtRa1VY607MsL_7ZUEFxb1WI-VS4gwVLQwpqLCsYwxdd2wSlA8y0bPmK35yAfmm_9QCcaTZnZuldc9fcUICK-xQVyPeGaIGT7F-cOeChoO1WSWkk2JPUyJEre466GPLnzVrmleDtZ_7oCmyf0E8YrBbwbT",
                  "width": 960,
                  "height": 960,
                  "precision": 1
                },
                "place": {
                  "url": "https://afisha.yandex.ru/q2a570P09/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj--Yqu2UxP0-oJLjSQFu-godTnJNuHwWET_6tOXkyw0iZx2QU3sqtMaJ5XYoE3Ms78yYEFJSf9a6u3V6Q4UaoTn433mr8zd8GpUk8f92rQnYba0S7Dgs9sJsKERlxFlPIAadElBJ6YbEede0C1AzjL-c2eEyoe-W-akXGrGX-AKqa-8J6DHkbQr0hXAvdzyI-N8eYx3pfffx3dpFV5baT9JnTzDTW1kUNtp19FkwM-3cD-tRQVEPdEtbRBjilrtAWCmPmMjylQ3apYVCPwTdO7i_7UDcO09EQ6xaRlVkKC2ShWzgA_vLlDbLV1W4gbHMnX6bs0HxX9fY2UT4ssd68nv77Dr74PQMieUVMVx2ntvJn91wXdheRzI-akbnxitcoLZ84WCquxY26NcV-YEB7bxs6jGQcV3U6asGyJNFa3J4WM8oKLF0DLu3FSBO9l3aaY5-AvyJ7GUR70nVBQTa7PJWfwFQCtpnpItHlShTI76uTRuSEkEstYmJ1MgBN2mAWBpcCQuzV93qlqWCPmYuGIlOXWFP21yUwL_45FS1CZzitExhYXsodBdolLd4UjNeb627YhICrsUayVS4YIX7Ang7rbubQwY-KjfEgnyV7qv6HV5wv0mPduGcqyUVR_jfkISvoXC4CzfFCWcHGNPxLO5uC-BCAU90a-tVSoGl6CBr-K46-gHlPWrEVsIctOxaG28MQBwqvpTD7Ut0NYW5v7DEXeKAufhnhFnEVIox0g-drNowoJEN56j5NBsDZ1qy61tNmzhhhc86BffxHIU8aGrszKM9u55Gga-IxYcWyW7whd_iY_t4tYSYtQWKkHJN3k470DNCjcd5GqWJgtSYoNpqrOhqoIc9aiV2kv_HndmrjVxATymsFfF8O5ZnhYreUDYu44FbyxRligS36JGAP25v6kLiAK-lKtq2q4DFaQBKip64OaOWLluHRjG_xE7aGI8P0z5JPoUR_nj0R-XajYKH_0Jh2ztGlZjn1nhTQs1tvYgDY2CNtRrbFRsR1wsiqChtSziwx34pFCXiHnQNaJhffxFcCHwV0pzYl6XG-F7w9e-AcMuZJMWZ5yWa47Dunc4acRMCzxfauiaq0yaZMVoLTcoqorft6oUlYfwkrsi4X-5wjSpMt8Fta9Z1h5ofojW_coDJqsXVSuV1ulHyDa-9qyFQot02yTq2m3DW6oKIS26qyoJkzBmEJQAM1g06uc7ugs4rzRQTDLmU54TIveC0DNJzGys05Xkl19lxEPwuzBozQRJuJtiJ19tAxRtjK5jO-gvyhl_YNbbBbSQ8-CtPHzDeSozUY21J55V0y5-AJp7ioHjoxAUaVHd4owJNTH74YkNBzLT7mUXLcPRKotvLrUuKARQ_SRXUoW8Fj2gr3Q1DXYs-5OBeWqUmhBhNYHato2I6yqZWqtcn2vOiDBxfqdExkg8FW6gXinPWeRLL2d6aCPD0P_i2d4PdNs0q-jx9QH4KvjSDTajnV-XIf4HEDMEy2fqGpct3VqsjEM4ffagxUmE8JKia58khllsyWSq-6nnRdg5Y9CbTPDfsi8ltDCKuWx30MGxKp2Y2yL2A5A7wkRi69-fY9-R5EcGsb_44IlKSfUXYamerUPcJciv6Drj6o1VvidYEkUwmzAnqDV2QDnp-ZfBNq9c35KquwMY90KDom5fVe-Q2iWHzLCxNmpOiYu_Giqhm2JEmW7K7eX17-pE0LIq1xiFfJFxY6L_d0U957hehjhnnRzarX9EX3ZCyaslWd5lENmtho-2P3PpAgyFO55tY5iiixKpjWYreq8mwl61LhWciTpXf69ler2Kfq01UYzzItnckWV6xZ01Rk8sY17XoxYR440JOn6_ZYWBS7-So6qbogDZKArkI_inIYxcvOPSmoWzkHct7zdyxH9uf1DHsGRSUh6hNUXQdwJP5CrbGmBaVynMC7l0_GyKwQuwX6doEiFDm2IGYK8_KeaOWb6rV19D81iwYW--vkB56fFZgjfmGFPeLLoC2rpDgifqmxwlF13owUT5f3JpAYUE9Z2nbxKqTFqoiWCh_KRqxhz8pd7dwbwU-69o-bECuWbxH0n2plUQ3ux1SV8zjgKqpZIdrZ2aYUcM_zy5L4qMArheayzdac1QYkVh6D4oYwxQOmMVG8Hx3LohrbNww3YtMxvAMm_Rn5cm-UMfdINCKmIXVi2VWepJBj10t2KBAE12nebqnSNPWW4LZWe3ZGPKWPpkX1COOdg3pe_8Ock-7_3bjD4umJSRJPzAUnNEQ-6rWZJql9IkgUx48fSqwUpPeFTl5R6tS5NrTSEmvC8jBBm1rdIQD7LU-msp8fBM92XxX0A66pza3ym3ip1zBM0kpdJeZ5aVpE6OMjYwZYmFwDqUZuUarEybZMUgLnWrokeefC2WmAdzkXJhpn-1BjVpO5RKNa0b31lpeovSdI7DLWWW1WHeHuUHxrE38e4LRkN8nGnjW23M2CLKaKozIeZHWb5vkRDE_xY8KeB9eQt1rP_bxfZoQ",
                  "width": 70,
                  "height": 70,
                  "precision": 1
                },
                "placeCover": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_4rmlk0EgYVedTnGWcudl92ie6SxkjQ645FLTk6oyQJ43RAylqRPbKpRcYQxBMb8z4QaNxb7frumcYAJY5citJnuhaI5V-axQlQU6Gf1oq_P4SDFmvVIBd62RXhEsMwMdegtHZ6mRkiKd2mMETfqz--rGRs0z0qxo3SEFnWYG7Cd36OENnbIm3ttJ-9jyY-e3uc63Yf1UR3MvW5PW63ZHGbTMj2Ng254hVF0rjkGwcbAgSM_MelKt7VNtz1ypxW-tvCGtBNG3K9USQHmccW4iNPiKt6m8m8G-LthfWew-jdd9Co9vaxBXqFfVpM0DMjuwIAxFS_yUpWhWqAzUq0QtI_IproWQ8C0dnQn3FL0npjG1iPZkMVLOP-pYn5vrssnau0JPbaGYWmyfGeTIjnf5uCCCREr4lmXs0uHK3-1EJS834KZFFvhrHZOFe1_wYaYxfMD2IHtRwjlqHhJRbvQBUjQGwSIqk5yt1JnrSEz2fH5pDAZJv97soJpmDFHlheCqt2vuR18wYNUSjzfbfGkpdDhGNKm5EA0y6R6f36O-wpVxRAXnbFTRbZcRJsiJMbQwpoNKwP_aryOd5I-R5IvpaPpp74bZ-irdkgjxET-obvs6w7Cost8P_yRSk5hh9Y0d9clK4mufFGBf0qnIzj05P-8EhAF93abpmupNmKSEb60-4ehNXXpmVd0E_xS6o-L2OQ35qTJbBDihm9ta7HlKlXwOy6bolhHg3tFgxw469H7qRglPNlUqZFXhCtsuxWXiMqhtC1ZwrB_fi3GTsyJhP3oLfWUynETxZ5TY1mo9ydx1BcVgItvSpd_XaMSDMPc26UPMCzTTq21aao1ZYYtlYXUmK0FQv6RXG0z0XvgmavY6iXjqv5bCNmISm1ugdQCRtksIL6CW3GddGKzDCbI5sW0JCsK81GKnmu3LEiSD7Og6JmfJWPhi1VjMPR-0Ki66_AG6Z7-ZjjiuG9UWZfdK0jRCBachF50oF9_qRIux-PqtQodE_99pb5WkQhQhA2So-iDpCxyx6l7SR_LTsGdr-zZMNSk5WIDyrVoWH-zyQJE5yIQoqZsWZd4XqUzP83Fz7UaEi3UcoeBUagvd4IpuI_ukJ8wXd6IRGstw1_guqbQ4CDcmsBoOci1YU5ioeoIZdg5JL-ien2CVFuqHD_u-964Kjcv31apsnaTOnO4KJqe1pmcKmLZs3lPL_VR4reUz9Aw2oXPQgborHFBRpHyElj-JACWgk9XpnxAkBMCxuTNuxY9Ce1YhqphiCtSoyOrn82viClj5q1jchXwXfW5vfPLKeaT0GEawYRuWmeX5g5f-DsHoa1PZYB1abMeNPrbw70hJwPwea28SqYOQoYZgr38pqkqYPOxfHcjy0XqgJv62S_Ak_J6I8GNT31fq_0tV8sKM4qSQliucGqHAhDY_eaGKRIJ1XOpqUizFXWrJbmn_7ONOlLQin12BPZdxZ6b8cMV8rjRTgfsk1h9bZPlIFH6NRethF9bgGtAkSce6__psDMVHsh4hYl6kwtzlBaLuMyciQ920qh0WTLxWteGuOvHMOe2wVwd_6ZPa0CW_xxayCszrplvV6B5QLI9Iv_4_ZELHjPrVZOucqoKQ5sina_DlI8oYMeMc3Q59HLgpI721RLDkcBOFd2QSnBqlOklRso1JKuESXaUe2OAPj397v67OiMc7Fa7qkmQIVyUK7Wa77SYFH3SoHp8DshC44KaxuMu6JDwZxDNu2J0foTQImPWDgesiWlphWZ9hD8V2MLklRAjEsxTt7BwhixugBGni_C8lxdD_b1kUzT1QdGYotrwJPih638r_qV1X0OJ-hZf_SMSv4hGSZNhdIgtD8Xa-LIIODP0fa2Bd7QecLcrt7jLmJsVbNO7elsW_WHMoKr9xzjgk8xjCfSMQmJ7jvc-WtAuCJGyeVitYEGBPQzk_O-FBQko3XmnjV64Ok22K4iM2JK9GGHak0hJJeNa0Ki-9OUv94rPQBTGjmVQa5TpBn_GMAG5tXtukHxqtDo76_3vnBA9A9lMmo1wgCxgphafhNiOvzRe3bl0SR7tbOGJq_zfCf2D8nE7_pN5bWCW1Qdk6TUAjLl4ba1SfJMMOd7By5oyFh3_VbqUf602TIIPqIvpgYA6WvaSREw551zGoJjnxCblgsVQPcWGUmpnq_oPds4mJp6EX0ede32POTvd3960MjUT022RnV-UAmKzMJOF3piBEFLSo3xeB8Jsxbi759kPyL3lQgvUj29OTojxNHf-FyO6qEdPi3ZJkCU8zvrlpS4_POhMuItKmyNjmzioodKmjyhB-rZlTwPvQcaBvtj_Osq7yXE875dYaFmu2QZkzgQzq5F_eqZddZEnB-bAypUaOiLrc7GgVYgeQKUFo6Pepp8sXdqIRUsgyVPDj6H-_ijqmMxnHMWpYX1ypuotSOY5LbeHZnmSWEmPDz_Bwdi5AxgP7laTrFKOMEurCLuD4r-YKlzXkHhpMdN604y-9_Y2yZb-eiXksWpG",
                  "width": 100,
                  "height": 100,
                  "precision": 1
                },
                "placeCoverXS": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_4rllk0EgqFSKm6RSJHQp_LfKeW07FwXxr5xTEaG-Dde_SAjvLNhVYNEaqYHFc7S6rkBIQHOf5qzT7IXQ6I2urz0laMwZf6ZQGk18GP2rJjP-CfTvvRZGcuLTGNOhPETfts4K5yATWaja2mKJSH62O-8BT4XwUaet36UMUyDGJCFzaakNFnTqFFvL-h-9rWA3fMM5KHpTAnYsFNDXaHZI3H9JQm0sWZvjEFTriAH-t75hTYVEP5IkJxRsQFpswykqumArSZV5L5caj_rX_GLm-n1A9ad9G8i45dLQ22O9gVV8wc0ubtvR4xAQYQ-HOL87ZIhGzD0TZqlaZEPbLYQv4jUppcFZMKuSV427GnGr6Xu5wDVlepeMtSOaENmpNYyRtA2NK-OeE-sQnmAOgzp_v-DBgMd7E26ln61LG6uMaeI7pSmKFHarkp7Fu147qOV9OYa4r__RRD2s3p6WIj5KUP-NgqshH5YtWRAiDcRy9vOoRkZJc9KrIB8mAxniRGIquq9lDph-JNfaQ3nX-ekqdrqGNSEym4f66ZxaU2T5B5C8BU8r5NheY5afboSEdrVwr8TFiXLcouJSJALYZI4oIjooo8Tbv2NY2Mb91vImKLt3yjlm8NDIcm0RFVZjMsKddMbAK6PU02zfGKBFBnG8uqjKB4Ay0yQnlqwFE-AOZKp1JK3BXrTvVdsItNdyoiN88gNxpH1cD_rk1pQS4DvHHfXFCSRj0x4t2lotC035MDdnwUDDuJIuaJrlgFXrBK7gd6sjRlc1bJyYDjAbcmVjtTQMcij7GIyz7d2a1Cp2BFj0wwEn7tkdZdlf6E9Pf7E-aErHQffcLuvda8Yf7cumqLNsposcMWdV2Iw1lP9v5XIxijGlMVBF_i6TV5uoOwqadgzFIGRb0-JdFS6Gx3h49KjNgQqy1KdikmuKl-WMYCrw7G_KUD0jGR4E9xn_YKl8_YN_6PTSD72smloTKbpL1TzLg6fmWBKpnV6jAIRzczynhAgMt1QvIlJtBFWhxeihemegBlRwZljUSXhXeaGntv7CvOF91wX-oRDbnKE2wJj1A8CvohqbIN1aoM8OsLuzZkpBxXbdJalT6cqSqgOg7rLrIgIcOaQX2g16WPDjKTZ-wPlmOV_Hdu7WFpvgM0mdvgKDZGISVKSeFqmPjHmwP6-EhIR4XW0tHeuKVCXCbiH766-BnLrokBYJe98zKab-eIT6rzVZwfmnUV-RqD4DFLQETeetWFNgXtmrBgD6O_mqQkDMPp-hbVsmD1TljamndKUuwpl5Yt8QzzTatOFh9DKDPGd03Mb4ZtaeXGP-D502TgUk4Ndco99UbYSHsnE8IInJiDfRKyXXZEcUJUjuoLXooASetytdVE69Wrxnr7Qwy3Wpe9oOOmoa01asPUDWtw7II-nf1SqRlmDGDvDwOWAMj0X8niXjV6EOECnAIGD1oW9ClXCrX5LAMdB0qqa_d061pfXcDXvmVRpfaboAHTHETaqqUxWpXBDhA8myOzFshIjEc1LpZJtqzx1gwKjivmzug1H2o5kTyXST8K4gO7oLcC60moJ5KtKTX672AxU1REVsJVYUbFRe48iBeX64rorIiHCf7OFYqM6UpUXh43UuL8lcPi4eV0H9mjDqojM3ijbkNB8MPipVFp7pv4tYNcyJ7OKWkeye0qyDQLm0uaBEQk-zXabsE6DLW6IAquE3I-DFXPerElrO91p84ON3PUA34TARTfdtW95fKveMnHKLCOyon9rqFVgsgMi4978uAcEDNlMiaFRiyJtti22mvO1vhZBxJRVeDHNWOibtu_rF_S5zW8D4Z5CbG-q8RJnzSUvoLhic7RyeKkiGs3Ezb81NhLudpmSaq8ub5kDsIT7l7Y2XPycck8t1WrPh5TlwiDJgcpiK-SzT3ZBkM4DWcwQJrC7Q1WjRXWYOTPJzsGWORIv73ampnmlCGKUCpi26aSoDUD0iHttOsJzzKSJ18AH-5HQfBPBpVF_aZfMNWTQOxO3jExUo1xgrBI3_PPBuAEEAv9Lsa55uQpOqw2yiumfpjtx1Z1zVxzIevGVpu_dG8aa0kAS2opUflybzzZZ_i00gY55aIdaQocMEeXT2LcsHi7bUoahSLY1QK8mmbrsuKwLVvyuaEwz0HvGtKDUyDDBne9vGsitR1hOpugcadcsKLSMenaSdEKkAj3d-NGXFSoA6m29r3-vNGqnAqiC_oaJO1XkjWhRGv1E5qaWxcEN5bTMZCHJnXZdaorwFH_aGDeoi2lTqWVeri0G_NHHghoLAcJlhotzkTpStCq9m--CpBZW3YhXdy__QsqVof7ZOsOj6kwT2q1lTXuzyCFS8SQ2qrBBaYZVaqszBcPY7J0JNiL8WI2Jf5EqVqgKg7vroYIEU9OXcXY932HPg4HU5wPWiOJ_OPaFWFNnpdEiZvQYKIKIZmiUeXOJHgDm-uCaDxgp8lWVqUOILVCpB5uGybCYLUPQiHh-I_xv_Z649f8I5r3haCnIuldG",
                  "width": 103,
                  "height": 103,
                  "precision": 1
                },
                "placeCoverM": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_43mlk0DgaFSKm6RSJHQp_LfKeW07FwXxr5xTEaG-Dde_SAjvLNhVYNEaqYHFc7S6rkBIQHOf5qzT7IXQ6I2urz0laMwZf6ZQGk18GP2rJjP-CfTvvRZGcuLTGNOhPETfts4K5yATWaja2mKJSH62O-8BT4XwUaet36UMUyDGJCFzaakNFnTqFFvL-h-9rWA3fMM5KHpTAnYsFNDXaHZI3H9JQm0sWZvjEFTriAH-t75hTYVEP5IkJxRsQFpswykqumArSZV5L5caj_rX_GLm-n1A9ad9G8i45dLQ22O9gVV8wc0ubtvR4xAQYQ-HOL87ZIhGzD0TZqlaZEPbLYQv4jUppcFZMKuSV427GnGr6Xu5wDVlepeMtSOaENmpNYyRtA2NK-OeE-sQnmAOgzp_v-DBgMd7E26ln61LG6uMaeI7pSmKFHarkp7Fu147qOV9OYa4r__RRD2s3p6WIj5KUP-NgqshH5YtWRAiDcRy9vOoRkZJc9KrIB8mAxniRGIquq9lDph-JNfaQ3nX-ekqdrqGNSEym4f66ZxaU2T5B5C8BU8r5NheY5afboSEdrVwr8TFiXLcouJSJALYZI4oIjooo8Tbv2NY2Mb91vImKLt3yjlm8NDIcm0RFVZjMsKddMbAK6PU02zfGKBFBnG8uqjKB4Ay0yQnlqwFE-AOZKp1JK3BXrTvVdsItNdyoiN88gNxpH1cD_rk1pQS4DvHHfXFCSRj0x4t2lotC035MDdnwUDDuJIuaJrlgFXrBK7gd6sjRlc1bJyYDjAbcmVjtTQMcij7GIyz7d2a1Cp2BFj0wwEn7tkdZdlf6E9Pf7E-aErHQffcLuvda8Yf7cumqLNsposcMWdV2Iw1lP9v5XIxijGlMVBF_i6TV5uoOwqadgzFIGRb0-JdFS6Gx3h49KjNgQqy1KdikmuKl-WMYCrw7G_KUD0jGR4E9xn_YKl8_YN_6PTSD72smloTKbpL1TzLg6fmWBKpnV6jAIRzczynhAgMt1QvIlJtBFWhxeihemegBlRwZljUSXhXeaGntv7CvOF91wX-oRDbnKE2wJj1A8CvohqbIN1aoM8OsLuzZkpBxXbdJalT6cqSqgOg7rLrIgIcOaQX2g16WPDjKTZ-wPlmOV_Hdu7WFpvgM0mdvgKDZGISVKSeFqmPjHmwP6-EhIR4XW0tHeuKVCXCbiH766-BnLrokBYJe98zKab-eIT6rzVZwfmnUV-RqD4DFLQETeetWFNgXtmrBgD6O_mqQkDMPp-hbVsmD1TljamndKUuwpl5Yt8QzzTatOFh9DKDPGd03Mb4ZtaeXGP-D502TgUk4Ndco99UbYSHsnE8IInJiDfRKyXXZEcUJUjuoLXooASetytdVE69Wrxnr7Qwy3Wpe9oOOmoa01asPUDWtw7II-nf1SqRlmDGDvDwOWAMj0X8niXjV6EOECnAIGD1oW9ClXCrX5LAMdB0qqa_d061pfXcDXvmVRpfaboAHTHETaqqUxWpXBDhA8myOzFshIjEc1LpZJtqzx1gwKjivmzug1H2o5kTyXST8K4gO7oLcC60moJ5KtKTX672AxU1REVsJVYUbFRe48iBeX64rorIiHCf7OFYqM6UpUXh43UuL8lcPi4eV0H9mjDqojM3ijbkNB8MPipVFp7pv4tYNcyJ7OKWkeye0qyDQLm0uaBEQk-zXabsE6DLW6IAquE3I-DFXPerElrO91p84ON3PUA34TARTfdtW95fKveMnHKLCOyon9rqFVgsgMi4978uAcEDNlMiaFRiyJtti22mvO1vhZBxJRVeDHNWOibtu_rF_S5zW8D4Z5CbG-q8RJnzSUvoLhic7RyeKkiGs3Ezb81NhLudpmSaq8ub5kDsIT7l7Y2XPycck8t1WrPh5TlwiDJgcpiK-SzT3ZBkM4DWcwQJrC7Q1WjRXWYOTPJzsGWORIv73ampnmlCGKUCpi26aSoDUD0iHttOsJzzKSJ18AH-5HQfBPBpVF_aZfMNWTQOxO3jExUo1xgrBI3_PPBuAEEAv9Lsa55uQpOqw2yiumfpjtx1Z1zVxzIevGVpu_dG8aa0kAS2opUflybzzZZ_i00gY55aIdaQocMEeXT2LcsHi7bUoahSLY1QK8mmbrsuKwLVvyuaEwz0HvGtKDUyDDBne9vGsitR1hOpugcadcsKLSMenaSdEKkAj3d-NGXFSoA6m29r3-vNGqnAqiC_oaJO1XkjWhRGv1E5qaWxcEN5bTMZCHJnXZdaorwFH_aGDeoi2lTqWVeri0G_NHHghoLAcJlhotzkTpStCq9m--CpBZW3YhXdy__QsqVof7ZOsOj6kwT2q1lTXuzyCFS8SQ2qrBBaYZVaqszBcPY7J0JNiL8WI2Jf5EqVqgKg7vroYIEU9OXcXY932HPg4HU5wPWiOJ_OPaFWFNnpdEiZvQYKIKIZmiUeXOJHgDm-uCaDxgp8lWVqUOILVCpB5uGybCYLUPQiHh-I_xv_Z649f8I5r3haCnIuldG",
                  "width": 170,
                  "height": 170,
                  "precision": 1
                },
                "touchPlace": {
                  "url": "https://avatars.mds.yandex.net/get-afishanew/35821/0f0465b1d24e2d04995ebe9be0a8ff59/80x80_noncrop",
                  "width": 80,
                  "height": 80,
                  "precision": 1
                },
                "touchPlaceCard": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_47mlk0AgYVedTnGWcudl92ie6SxkjQ645FLTk6oyQJ43RAylqRPbKpRcYQxBMb8z4QaNxb7frumcYAJY5citJnuhaI5V-axQlQU6Gf1oq_P4SDFmvVIBd62RXhEsMwMdegtHZ6mRkiKd2mMETfqz--rGRs0z0qxo3SEFnWYG7Cd36OENnbIm3ttJ-9jyY-e3uc63Yf1UR3MvW5PW63ZHGbTMj2Ng254hVF0rjkGwcbAgSM_MelKt7VNtz1ypxW-tvCGtBNG3K9USQHmccW4iNPiKt6m8m8G-LthfWew-jdd9Co9vaxBXqFfVpM0DMjuwIAxFS_yUpWhWqAzUq0QtI_IproWQ8C0dnQn3FL0npjG1iPZkMVLOP-pYn5vrssnau0JPbaGYWmyfGeTIjnf5uCCCREr4lmXs0uHK3-1EJS834KZFFvhrHZOFe1_wYaYxfMD2IHtRwjlqHhJRbvQBUjQGwSIqk5yt1JnrSEz2fH5pDAZJv97soJpmDFHlheCqt2vuR18wYNUSjzfbfGkpdDhGNKm5EA0y6R6f36O-wpVxRAXnbFTRbZcRJsiJMbQwpoNKwP_aryOd5I-R5IvpaPpp74bZ-irdkgjxET-obvs6w7Cost8P_yRSk5hh9Y0d9clK4mufFGBf0qnIzj05P-8EhAF93abpmupNmKSEb60-4ehNXXpmVd0E_xS6o-L2OQ35qTJbBDihm9ta7HlKlXwOy6bolhHg3tFgxw469H7qRglPNlUqZFXhCtsuxWXiMqhtC1ZwrB_fi3GTsyJhP3oLfWUynETxZ5TY1mo9ydx1BcVgItvSpd_XaMSDMPc26UPMCzTTq21aao1ZYYtlYXUmK0FQv6RXG0z0XvgmavY6iXjqv5bCNmISm1ugdQCRtksIL6CW3GddGKzDCbI5sW0JCsK81GKnmu3LEiSD7Og6JmfJWPhi1VjMPR-0Ki66_AG6Z7-ZjjiuG9UWZfdK0jRCBachF50oF9_qRIux-PqtQodE_99pb5WkQhQhA2So-iDpCxyx6l7SR_LTsGdr-zZMNSk5WIDyrVoWH-zyQJE5yIQoqZsWZd4XqUzP83Fz7UaEi3UcoeBUagvd4IpuI_ukJ8wXd6IRGstw1_guqbQ4CDcmsBoOci1YU5ioeoIZdg5JL-ien2CVFuqHD_u-964Kjcv31apsnaTOnO4KJqe1pmcKmLZs3lPL_VR4reUz9Aw2oXPQgborHFBRpHyElj-JACWgk9XpnxAkBMCxuTNuxY9Ce1YhqphiCtSoyOrn82viClj5q1jchXwXfW5vfPLKeaT0GEawYRuWmeX5g5f-DsHoa1PZYB1abMeNPrbw70hJwPwea28SqYOQoYZgr38pqkqYPOxfHcjy0XqgJv62S_Ak_J6I8GNT31fq_0tV8sKM4qSQliucGqHAhDY_eaGKRIJ1XOpqUizFXWrJbmn_7ONOlLQin12BPZdxZ6b8cMV8rjRTgfsk1h9bZPlIFH6NRethF9bgGtAkSce6__psDMVHsh4hYl6kwtzlBaLuMyciQ920qh0WTLxWteGuOvHMOe2wVwd_6ZPa0CW_xxayCszrplvV6B5QLI9Iv_4_ZELHjPrVZOucqoKQ5sina_DlI8oYMeMc3Q59HLgpI721RLDkcBOFd2QSnBqlOklRso1JKuESXaUe2OAPj397v67OiMc7Fa7qkmQIVyUK7Wa77SYFH3SoHp8DshC44KaxuMu6JDwZxDNu2J0foTQImPWDgesiWlphWZ9hD8V2MLklRAjEsxTt7BwhixugBGni_C8lxdD_b1kUzT1QdGYotrwJPih638r_qV1X0OJ-hZf_SMSv4hGSZNhdIgtD8Xa-LIIODP0fa2Bd7QecLcrt7jLmJsVbNO7elsW_WHMoKr9xzjgk8xjCfSMQmJ7jvc-WtAuCJGyeVitYEGBPQzk_O-FBQko3XmnjV64Ok22K4iM2JK9GGHak0hJJeNa0Ki-9OUv94rPQBTGjmVQa5TpBn_GMAG5tXtukHxqtDo76_3vnBA9A9lMmo1wgCxgphafhNiOvzRe3bl0SR7tbOGJq_zfCf2D8nE7_pN5bWCW1Qdk6TUAjLl4ba1SfJMMOd7By5oyFh3_VbqUf602TIIPqIvpgYA6WvaSREw551zGoJjnxCblgsVQPcWGUmpnq_oPds4mJp6EX0ede32POTvd3960MjUT022RnV-UAmKzMJOF3piBEFLSo3xeB8Jsxbi759kPyL3lQgvUj29OTojxNHf-FyO6qEdPi3ZJkCU8zvrlpS4_POhMuItKmyNjmzioodKmjyhB-rZlTwPvQcaBvtj_Osq7yXE875dYaFmu2QZkzgQzq5F_eqZddZEnB-bAypUaOiLrc7GgVYgeQKUFo6Pepp8sXdqIRUsgyVPDj6H-_ijqmMxnHMWpYX1ypuotSOY5LbeHZnmSWEmPDz_Bwdi5AxgP7laTrFKOMEurCLuD4r-YKlzXkHhpMdN604y-9_Y2yZb-eiXksWpG",
                  "width": 140,
                  "height": 140,
                  "precision": 1
                },
                "touchPlaceCover": {
                  "url": "https://avatars.mds.yandex.net/get-afishanew/35821/0f0465b1d24e2d04995ebe9be0a8ff59/220x220_noncrop",
                  "width": 220,
                  "height": 220,
                  "precision": 1
                },
                "touchConcertPlace": {
                  "url": "https://afisha.yandex.ru/q2a571P07/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-vYLulkQMyrgAI2PGHpmmofL5N_aZ8m8ZzI1XVU2HzypS3icBiotBWLNpVJAWNMjUwrIyFjLbWaiwSK0eZZYKo4D5m6Ite_KqQ3gC7XnlmZzV9wH8gfdhFPmweF1PjusKdMYvIbmncnicaniyIgDC0ce2LQA94l2sgW6LEUS4IJq5ypymEVbDu0ViGvB5_IGO3tw245zicQfCr1hOaqbbBVLbDQmIjHtXtlBctwQAxMf-hQYHAuxTh65LuzR0rBS1neyVtB1h1bZAchnRfsKautjTBN-BwVo85bdYfkWJ_SFc-TAEgoVTV7dCdqkfGObT6ZIIJwjpWb6Wa7UxcbAPl6DKr5csR8WjdHse50nmpL3K0AfXn_BKC_yUWHVvqcoyf8gwEreSW3e1enKtDxPkwfi1EAoQ6XmNgU-WM2mRF5ea-J66GV_FoFFbH_Zh6pSny8ow_YrraCnBhmFLQ4bRN1HIDhG9lExuk0N6oBIxwfDaqgoyM-5vm4NitjpOsTi1ntGsqCl9-LVDQBXRaO2oicfIBsa_wGc01I1yXlib5jZf6zgSqottVa1-SIUSIM_8xKAFMjfWSJK3arE8VZgQl5zOt4EmeOaJSVYF1UfRo77y-DfZtu1ZFsa4TkpHtPIBfOUEE7a5WWiLYXODGjzo1NibDRc36FOFpUquEkeZIrag_o-XMlbWvUZvIdNFwYyg5d0U04DeRzThpktYS5DkA3jqICy2pmxsnmtGujQe2uPkthAZHux6uZRsuwprsgueqsC1ixRQ2ZhKdTLjRtyPh_3hGuGZzEoQxYpwQ2Kn6Rd88gAigo5hTJJ8U6o-BN7H2pgOECPUeLSKVaIicI4qvbneor44QPa9SH0k3XL2lJvr-BTWsO9vJ8ixRX1rk9Idd80QPKiFW1KDV0iMHhv57NiFFz039l6RtlSQAlGRMLS33Ye7CHHnjlJeLulyy6Sg290t4abmRinAlXNfbZbXIFzQCiKgil59gnl-lRI31szlozMlIfR_krZOqwtAtxKanfK4ixlE8ol7aBPTac-fiNbaIceC8m8l9r91YU-k-hd78QYDsYB4WIJpcas5OPTz4poUAifQVb6wXZAXb64zpb_AsJo4Y_u1Qngb7UzFpYrW0zfakNFlBMmkQXxLst4CV_QJLLGjRkmPWVSpMhzawMWhAQYd0XeviFSTDVCpCJibwoaUOm7JqnJoHfJD75qqz8M4_qDJfznvuWVVa4f0Jn_vMyOMi1lajGVejwAS9djSuhAnBtpGrpNihw5RlhaCpviDmC1g4JZpcSHkXMyGg-fcI9-m3WM-6aZiYkSHxgB2xhAuurdmVIpSRIUdM97O-ZQ1NyPgb4yia6YNUoMKnaPOuIAyWcafe3cH5H7Xv4Pu_QTnmsZANtqXVkl7ivsuc8UkMp6VQHGxWnGPODna2_uBLgAO3FSWoX6CHWCgMZyi6YWYHUfGlGFNNc9d45uu8OoE1aLeTTDrqHJubZf4AGjvMheQpkJ-h0B2mCUy9vvJoTAGMe9miZJRhihEohOVjd-Cnw9f5Y5laCDBTfGBvcX9EvinxHE72bZWbXCn9CB67xENrLJFaqZ4fbUGH-DcwZgxNj7bcJ6dWYAPUrc3kqDUh7c4fdOTd0oE5kzjiZ_z-AnSpdJIJ9uoQWhtgdUUeMwjDrOwU2mMSUCaARzI2PqiGikx0lirsXmXM0-iG5uo47uHO1vHo0F2L-d8yoyP2NANxrXrTwLHk2JvYKHKBWXSJw-blX9zomNAlCEZxMLDtBcbJehKuq5xmDBxjQaFh9mGhAlB_79SfD_WZ9K3vMbHJvu4wXs-7L53fGGO6hNi2ysdgYhnb4V7W7UZN97zxIYlBRLSWomVVZQyXqMAm4_7jqQUefeYZWAn5EDOlbbv8BvDv8xTO8GzbVJbsfstY-4iDYKpQXiydmquMDPU_-2KATgT0mW9hl-yP1OqKKmdyJCfCHHjkUd3MP1D7YiE7dcp06XSax7XrWR6XLPNEH_FFwq1pkB4q2NehTQG6f_DshcVA-9ytYZDsBNsrQKVnfOeqTlQ9pl9UTr0ftynvPDLFNin7moF-KhlT1Cwzi1R0zA8t5N8XK1BdZsSH8nmzJ8NOSf2Rbq3TI8daIYppZjUlJkeecWCZn4i9Un9oYfl4BPfmsFiF9-7Q11tl-QdeNIsCbWQYkmDQVaVPifi7-ymORcWyX60gFWON2CiGJ2K6rGpHWHmgntXD8pp75eW7N039rnKWRbvikZ5QY_sC3XmMxWyg0dykl1cugUGy_n5qRgWPsFFkIxrgA9zig2Em-6chB5Y471dYg3MRdygrfTqEeGf4msF35lWaHi32SZe2jIXiat9XaJpWaQGOcLS5rolNQD8TpKAa5ALb6ozpJ_NupYbVvybXHAt70DKgIfK0wTKl9FAKfekSHRurtoSW-YsP7GMfE-OcHuJAxzg3uG8Cz4O8VayvHKXDW6nK5m93KC_C1XjklRuDuFy17mm0tg0_5TGURfIq10",
                  "width": 88,
                  "height": 88,
                  "precision": 1
                }
              },
              "address": "Комсомольский просп., 28",
              "type": {
                "id": "5575d419cc1c724f5a8e1125",
                "rubricUrl": "/moscow/concert_hall",
                "code": "concert_hall",
                "type": "place",
                "status": "approved",
                "name": "Концертный зал",
                "namePlural": "концертные залы",
                "nameAcc": "в концертный зал",
                "nameGen": null,
                "nameAdj": null,
                "plural": null,
                "rubricPlacesUrl": "/moscow/concert_hall/places"
              },
              "tags": [
                {
                  "id": "5575d419cc1c724f5a8e1125",
                  "rubricUrl": "/moscow/concert_hall",
                  "code": "concert_hall",
                  "type": "place",
                  "status": "approved",
                  "name": "Концертный зал",
                  "namePlural": "концертные залы",
                  "nameAcc": "в концертный зал",
                  "nameGen": null,
                  "nameAdj": null,
                  "plural": null,
                  "rubricPlacesUrl": "/moscow/concert_hall/places"
                },
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
                  "code": "concert_hall"
                },
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
                  "name": "Фрунзенская",
                  "colors": [
                    "#cc0000"
                  ]
                },
                {
                  "name": "Спортивная",
                  "colors": [
                    "#cc0000"
                  ]
                },
                {
                  "name": "Парк культуры",
                  "colors": [
                    "#7f0000"
                  ]
                }
              ],
              "coordinates": {
                "longitude": 37.57964499999999,
                "latitude": 55.726876999999995
              },
              "bgColor": "#4b4b75",
              "logoColor": "#7c7cc2",
              "distance": null,
              "isFavorite": false
            },
            "headliners": {
              "title": null,
              "description": null
            },
            "session": {
              "date": "2118-11-11",
              "datetime": "2118-11-11T13:00:00",
              "ticket": {
                "id": "ODQ2fDk3MTM3fDEzMjg2MHwxNTQxOTMwNDAwMDAw",
                "price": {
                  "currency": "rub",
                  "min": 140000,
                  "max": 480000
                },
                "discountPercents": []
              },
              "hall": null
            }
          },
          {
            "place": {
              "id": "5516a4171f7d154a12dc66a1",
              "url": "/moscow/theatre/places/mdm-5516a4171f7d154a12dc66a1",
              "title": "МДМ",
              "logo": {
                "bgColor": "#4d4d4d",
                "microdata": {
                  "url": "https://afisha.yandex.ru/q2a568P13/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-oci_iQdWgeMEeWKYYOmgh8r0CcW0z2sg2bJFX3ut3gV2-zMPkqZ8RaBhc6AxNOb3-rY2MAHPaKyoXoIMbbMvkoP2h6E_RMK4ZVIF5F_Uh4n8_hHAusJeHfa6R1ZfjfgdftsAI6GGU0aMQ0eUOzHj8-WgOQkFy1mKjlGjIkeKFqGE8ruMDlXEon1PBf1Hxoyiy-EM1arRZQLWqWJ-b4LeAFzzMQioqXl8qEZhlD0n2sDOpwYHC-B2r750kzZzpTKHjeC3uxhYwbJ-bgLDXPKKrfndEfaB6kIa1plNUUmm0CJh_jsBgKl4boJYeowfM83XwIcMAgHZTo-wcZYqaIcPobfDhp0ITfW7eVg152L1mK761Q_Hkd1bOdaSZ3F-tfMTYegOFoiJelaGXGqHHSHc8NiqFAIh6lmrk3OOC3CHNZOG7rOFCE7Qm3hJHetS75m0zf8a3LP_ZivvrEteZbDdE1_rBBCfkFxvjlF3pTgQ_u_CkjcFN_xbhrN6qStfpTG6tPyDpzVbwoBybhTsbsGVtvvEL_e84nMg_LlQQ1Kx0zBp6BMPvqtiUrx0d7Q2HODlzZIzPRD1b460fLICd4czpa_VjKIrZ8iWYmo70GX2oIbK2ybagsBhFcCtT2xGhvA-VekPPYqWRE2Hcn-oETT83sW3MwML4n2uq1KgA0WmD5WXw5iMG1PHr0ZsOcBK6Lej6dEQ6ZziRgvFv0NIUIT0MXHWDyK_klFHsktRiiMDwPPYuRoHIt5MiL5KjChsjgWrrd--ihR2y7VVXDrdSc-vn-fjCfuRxmIn_qRqf12Q8ClR2DsKsrJdUKdbW5AnJ_7dxrAnPyDTUrGnYpcUTa0Wtbrqkpo7U8m9Q2IO91LTuYbp1CDYtPFvHMuaY0tmmvsWQcYRAYisTHu8fXuPAAz8wN-dMx0G9m6wlUK2C1ekGLaf76KrKmDTnklWDspi6Imj0OM20Z3_Zzj9uGVOY6fQC1vYGQ6Ng01VimR3oy8sweb7hSUfJ_Vuqq5Lpy11ijKZoN-znj9n-qh0bBXOWcCEpNzFEsW081ES-4ZHfE6Q9ypX-QgEq6ZNRYVaXKwNE8bf3KIjOw3ZaLmVV4g0VLUQq6jOkrk2W8O4fFIwxGPChK3K2ADmvtJuCc-bQ2pqhdsvWNYIJ5W3QHWgWFeIIyDh5MmmGTovyFCwlk23M2-INKmewJC0BETzqHpNP-5c4p29xfww_qTvSBTrsmNfQKHzNGLZNQ-KpENJqn5lhgw49v_YhwIxHslLhoJOtgxxkgmTm8yHui146LFGWyDNQMu1ot7dNuq46E4L7IVMX3KH-h1B1AMztapFfrB0eKcnLt3R_ZcnCzfreo-jTbUZbY0MpaDUmIMLcfq3YFsC1nnLvIP55Qrxm-B9Otiuc1JPqf8edcgnEZOPfnaFfl2tIzvfxOagCjcM8Xmah12HOlaMDYKdzLedC3rgjVJwIeJd5qKU-dcy6ZbmTAX8iWVPTIfkNGPtKSKRgEhsgmlApg8b7eT4pjUEPu5KtYNoozh0hSK0msulhShg5KhHfjHwR_WXg-_6N_Oq7X4b2Ip4f0Cn9jRA9xU2lpRpVIlEY4sZPOXd-ZY6MCj5Rb2FT7UtUIIPv5_jkqceffaKY1kw4k_XoYb00DXlk_F8Bc-PZVlhk_QXcvQKNICXQ2W0a2SIMTje59KJNTkAzGmdknOoOHyLB4ij05GBCk3AtkhYAMtKx4qu8MQl3JTUYD7siGh5foLpCXb1IhGsjW1PtGVEjT0i5_HfuyEDEt12lZ1wlhdhlSiyntCjmzJR07xYaRvTcfSUudv5KPag6EsT-ZtpVl6U7gB65zgMtJFKV69EfKMnE-DD7aUWOQLuTbGRcrk5Z4sgkJbwvqM6duSgQFs8z1P-vY7mwS_7iO1mHuO1U2lPqu81c_c7LZKGfVqeX1WnLR_Jz8mYFzk92l67t3-0ME-5MqOIy6KrLn_Gt1dCP-xOzL-p1NE15bDIcADqnVRreZfzHkbwDCKThmRPqnRRkhAf5_fftQcEKtJep7VTizdlhTKYhv2Tijt3_JFdSwLdYfSitenaN9mx018F66hYaHqq3Qhhxg4Xr6JibYFqd4swBujaxZkjHR3db6iKXY8cTrU3v4zNtKMIbOe-RUo1_GfPt57u3Qr2ucF4Fs26ZU9QmvQJffMMFLG3TG2iZFuzGw_I4_G3EiIm01ixi3eHOH-NJYGp_be7K2z6l2h1Fe5R3r6jyvQp_YLASCfInklXWIz5PWLvCweUjF1xqEtgkjIZ3ezQtjoqHfdUj4VPlBBqlDSFhNC0gi5T3KJqczndZuWmlOzjD9Ww03g02I9wb22h0gFj7TAvrqNtRa1VY607MsL_7ZUEFxb1WI-VS4gwVLQwpqLCsYwxdd2wSlA8y0bPmK35yAfmm_9QCcaTZnZuldc9fcUICK-xQVyPeGaIGT7F-cOeChoO1WSWkk2JPUyJEre466GPLnzVrmleDtZ_7oCmyf0E8YrBbwbT",
                  "width": 960,
                  "height": 960,
                  "precision": 1
                },
                "place": {
                  "url": "https://afisha.yandex.ru/q2a570P09/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj--Yqu2UxP0-oJLjSQFu-godTnJNuHwWET_6tOXkyw0iZx2QU3sqtMaJ5XYoE3Ms78yYEFJSf9a6u3V6Q4UaoTn433mr8zd8GpUk8f92rQnYba0S7Dgs9sJsKERlxFlPIAadElBJ6YbEede0C1AzjL-c2eEyoe-W-akXGrGX-AKqa-8J6DHkbQr0hXAvdzyI-N8eYx3pfffx3dpFV5baT9JnTzDTW1kUNtp19FkwM-3cD-tRQVEPdEtbRBjilrtAWCmPmMjylQ3apYVCPwTdO7i_7UDcO09EQ6xaRlVkKC2ShWzgA_vLlDbLV1W4gbHMnX6bs0HxX9fY2UT4ssd68nv77Dr74PQMieUVMVx2ntvJn91wXdheRzI-akbnxitcoLZ84WCquxY26NcV-YEB7bxs6jGQcV3U6asGyJNFa3J4WM8oKLF0DLu3FSBO9l3aaY5-AvyJ7GUR70nVBQTa7PJWfwFQCtpnpItHlShTI76uTRuSEkEstYmJ1MgBN2mAWBpcCQuzV93qlqWCPmYuGIlOXWFP21yUwL_45FS1CZzitExhYXsodBdolLd4UjNeb627YhICrsUayVS4YIX7Ang7rbubQwY-KjfEgnyV7qv6HV5wv0mPduGcqyUVR_jfkISvoXC4CzfFCWcHGNPxLO5uC-BCAU90a-tVSoGl6CBr-K46-gHlPWrEVsIctOxaG28MQBwqvpTD7Ut0NYW5v7DEXeKAufhnhFnEVIox0g-drNowoJEN56j5NBsDZ1qy61tNmzhhhc86BffxHIU8aGrszKM9u55Gga-IxYcWyW7whd_iY_t4tYSYtQWKkHJN3k470DNCjcd5GqWJgtSYoNpqrOhqoIc9aiV2kv_HndmrjVxATymsFfF8O5ZnhYreUDYu44FbyxRligS36JGAP25v6kLiAK-lKtq2q4DFaQBKip64OaOWLluHRjG_xE7aGI8P0z5JPoUR_nj0R-XajYKH_0Jh2ztGlZjn1nhTQs1tvYgDY2CNtRrbFRsR1wsiqChtSziwx34pFCXiHnQNaJhffxFcCHwV0pzYl6XG-F7w9e-AcMuZJMWZ5yWa47Dunc4acRMCzxfauiaq0yaZMVoLTcoqorft6oUlYfwkrsi4X-5wjSpMt8Fta9Z1h5ofojW_coDJqsXVSuV1ulHyDa-9qyFQot02yTq2m3DW6oKIS26qyoJkzBmEJQAM1g06uc7ugs4rzRQTDLmU54TIveC0DNJzGys05Xkl19lxEPwuzBozQRJuJtiJ19tAxRtjK5jO-gvyhl_YNbbBbSQ8-CtPHzDeSozUY21J55V0y5-AJp7ioHjoxAUaVHd4owJNTH74YkNBzLT7mUXLcPRKotvLrUuKARQ_SRXUoW8Fj2gr3Q1DXYs-5OBeWqUmhBhNYHato2I6yqZWqtcn2vOiDBxfqdExkg8FW6gXinPWeRLL2d6aCPD0P_i2d4PdNs0q-jx9QH4KvjSDTajnV-XIf4HEDMEy2fqGpct3VqsjEM4ffagxUmE8JKia58khllsyWSq-6nnRdg5Y9CbTPDfsi8ltDCKuWx30MGxKp2Y2yL2A5A7wkRi69-fY9-R5EcGsb_44IlKSfUXYamerUPcJciv6Drj6o1VvidYEkUwmzAnqDV2QDnp-ZfBNq9c35KquwMY90KDom5fVe-Q2iWHzLCxNmpOiYu_Giqhm2JEmW7K7eX17-pE0LIq1xiFfJFxY6L_d0U957hehjhnnRzarX9EX3ZCyaslWd5lENmtho-2P3PpAgyFO55tY5iiixKpjWYreq8mwl61LhWciTpXf69ler2Kfq01UYzzItnckWV6xZ01Rk8sY17XoxYR440JOn6_ZYWBS7-So6qbogDZKArkI_inIYxcvOPSmoWzkHct7zdyxH9uf1DHsGRSUh6hNUXQdwJP5CrbGmBaVynMC7l0_GyKwQuwX6doEiFDm2IGYK8_KeaOWb6rV19D81iwYW--vkB56fFZgjfmGFPeLLoC2rpDgifqmxwlF13owUT5f3JpAYUE9Z2nbxKqTFqoiWCh_KRqxhz8pd7dwbwU-69o-bECuWbxH0n2plUQ3ux1SV8zjgKqpZIdrZ2aYUcM_zy5L4qMArheayzdac1QYkVh6D4oYwxQOmMVG8Hx3LohrbNww3YtMxvAMm_Rn5cm-UMfdINCKmIXVi2VWepJBj10t2KBAE12nebqnSNPWW4LZWe3ZGPKWPpkX1COOdg3pe_8Ock-7_3bjD4umJSRJPzAUnNEQ-6rWZJql9IkgUx48fSqwUpPeFTl5R6tS5NrTSEmvC8jBBm1rdIQD7LU-msp8fBM92XxX0A66pza3ym3ip1zBM0kpdJeZ5aVpE6OMjYwZYmFwDqUZuUarEybZMUgLnWrokeefC2WmAdzkXJhpn-1BjVpO5RKNa0b31lpeovSdI7DLWWW1WHeHuUHxrE38e4LRkN8nGnjW23M2CLKaKozIeZHWb5vkRDE_xY8KeB9eQt1rP_bxfZoQ",
                  "width": 70,
                  "height": 70,
                  "precision": 1
                },
                "placeCover": {
                  "url": "https://avatars.mds.yandex.net/get-afishanew/35821/0f0465b1d24e2d04995ebe9be0a8ff59/100x100_noncrop",
                  "width": 100,
                  "height": 100,
                  "precision": 1
                },
                "placeCoverXS": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_4rllk0EgqFSKm6RSJHQp_LfKeW07FwXxr5xTEaG-Dde_SAjvLNhVYNEaqYHFc7S6rkBIQHOf5qzT7IXQ6I2urz0laMwZf6ZQGk18GP2rJjP-CfTvvRZGcuLTGNOhPETfts4K5yATWaja2mKJSH62O-8BT4XwUaet36UMUyDGJCFzaakNFnTqFFvL-h-9rWA3fMM5KHpTAnYsFNDXaHZI3H9JQm0sWZvjEFTriAH-t75hTYVEP5IkJxRsQFpswykqumArSZV5L5caj_rX_GLm-n1A9ad9G8i45dLQ22O9gVV8wc0ubtvR4xAQYQ-HOL87ZIhGzD0TZqlaZEPbLYQv4jUppcFZMKuSV427GnGr6Xu5wDVlepeMtSOaENmpNYyRtA2NK-OeE-sQnmAOgzp_v-DBgMd7E26ln61LG6uMaeI7pSmKFHarkp7Fu147qOV9OYa4r__RRD2s3p6WIj5KUP-NgqshH5YtWRAiDcRy9vOoRkZJc9KrIB8mAxniRGIquq9lDph-JNfaQ3nX-ekqdrqGNSEym4f66ZxaU2T5B5C8BU8r5NheY5afboSEdrVwr8TFiXLcouJSJALYZI4oIjooo8Tbv2NY2Mb91vImKLt3yjlm8NDIcm0RFVZjMsKddMbAK6PU02zfGKBFBnG8uqjKB4Ay0yQnlqwFE-AOZKp1JK3BXrTvVdsItNdyoiN88gNxpH1cD_rk1pQS4DvHHfXFCSRj0x4t2lotC035MDdnwUDDuJIuaJrlgFXrBK7gd6sjRlc1bJyYDjAbcmVjtTQMcij7GIyz7d2a1Cp2BFj0wwEn7tkdZdlf6E9Pf7E-aErHQffcLuvda8Yf7cumqLNsposcMWdV2Iw1lP9v5XIxijGlMVBF_i6TV5uoOwqadgzFIGRb0-JdFS6Gx3h49KjNgQqy1KdikmuKl-WMYCrw7G_KUD0jGR4E9xn_YKl8_YN_6PTSD72smloTKbpL1TzLg6fmWBKpnV6jAIRzczynhAgMt1QvIlJtBFWhxeihemegBlRwZljUSXhXeaGntv7CvOF91wX-oRDbnKE2wJj1A8CvohqbIN1aoM8OsLuzZkpBxXbdJalT6cqSqgOg7rLrIgIcOaQX2g16WPDjKTZ-wPlmOV_Hdu7WFpvgM0mdvgKDZGISVKSeFqmPjHmwP6-EhIR4XW0tHeuKVCXCbiH766-BnLrokBYJe98zKab-eIT6rzVZwfmnUV-RqD4DFLQETeetWFNgXtmrBgD6O_mqQkDMPp-hbVsmD1TljamndKUuwpl5Yt8QzzTatOFh9DKDPGd03Mb4ZtaeXGP-D502TgUk4Ndco99UbYSHsnE8IInJiDfRKyXXZEcUJUjuoLXooASetytdVE69Wrxnr7Qwy3Wpe9oOOmoa01asPUDWtw7II-nf1SqRlmDGDvDwOWAMj0X8niXjV6EOECnAIGD1oW9ClXCrX5LAMdB0qqa_d061pfXcDXvmVRpfaboAHTHETaqqUxWpXBDhA8myOzFshIjEc1LpZJtqzx1gwKjivmzug1H2o5kTyXST8K4gO7oLcC60moJ5KtKTX672AxU1REVsJVYUbFRe48iBeX64rorIiHCf7OFYqM6UpUXh43UuL8lcPi4eV0H9mjDqojM3ijbkNB8MPipVFp7pv4tYNcyJ7OKWkeye0qyDQLm0uaBEQk-zXabsE6DLW6IAquE3I-DFXPerElrO91p84ON3PUA34TARTfdtW95fKveMnHKLCOyon9rqFVgsgMi4978uAcEDNlMiaFRiyJtti22mvO1vhZBxJRVeDHNWOibtu_rF_S5zW8D4Z5CbG-q8RJnzSUvoLhic7RyeKkiGs3Ezb81NhLudpmSaq8ub5kDsIT7l7Y2XPycck8t1WrPh5TlwiDJgcpiK-SzT3ZBkM4DWcwQJrC7Q1WjRXWYOTPJzsGWORIv73ampnmlCGKUCpi26aSoDUD0iHttOsJzzKSJ18AH-5HQfBPBpVF_aZfMNWTQOxO3jExUo1xgrBI3_PPBuAEEAv9Lsa55uQpOqw2yiumfpjtx1Z1zVxzIevGVpu_dG8aa0kAS2opUflybzzZZ_i00gY55aIdaQocMEeXT2LcsHi7bUoahSLY1QK8mmbrsuKwLVvyuaEwz0HvGtKDUyDDBne9vGsitR1hOpugcadcsKLSMenaSdEKkAj3d-NGXFSoA6m29r3-vNGqnAqiC_oaJO1XkjWhRGv1E5qaWxcEN5bTMZCHJnXZdaorwFH_aGDeoi2lTqWVeri0G_NHHghoLAcJlhotzkTpStCq9m--CpBZW3YhXdy__QsqVof7ZOsOj6kwT2q1lTXuzyCFS8SQ2qrBBaYZVaqszBcPY7J0JNiL8WI2Jf5EqVqgKg7vroYIEU9OXcXY932HPg4HU5wPWiOJ_OPaFWFNnpdEiZvQYKIKIZmiUeXOJHgDm-uCaDxgp8lWVqUOILVCpB5uGybCYLUPQiHh-I_xv_Z649f8I5r3haCnIuldG",
                  "width": 103,
                  "height": 103,
                  "precision": 1
                },
                "placeCoverM": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_43mlk0DgaFSKm6RSJHQp_LfKeW07FwXxr5xTEaG-Dde_SAjvLNhVYNEaqYHFc7S6rkBIQHOf5qzT7IXQ6I2urz0laMwZf6ZQGk18GP2rJjP-CfTvvRZGcuLTGNOhPETfts4K5yATWaja2mKJSH62O-8BT4XwUaet36UMUyDGJCFzaakNFnTqFFvL-h-9rWA3fMM5KHpTAnYsFNDXaHZI3H9JQm0sWZvjEFTriAH-t75hTYVEP5IkJxRsQFpswykqumArSZV5L5caj_rX_GLm-n1A9ad9G8i45dLQ22O9gVV8wc0ubtvR4xAQYQ-HOL87ZIhGzD0TZqlaZEPbLYQv4jUppcFZMKuSV427GnGr6Xu5wDVlepeMtSOaENmpNYyRtA2NK-OeE-sQnmAOgzp_v-DBgMd7E26ln61LG6uMaeI7pSmKFHarkp7Fu147qOV9OYa4r__RRD2s3p6WIj5KUP-NgqshH5YtWRAiDcRy9vOoRkZJc9KrIB8mAxniRGIquq9lDph-JNfaQ3nX-ekqdrqGNSEym4f66ZxaU2T5B5C8BU8r5NheY5afboSEdrVwr8TFiXLcouJSJALYZI4oIjooo8Tbv2NY2Mb91vImKLt3yjlm8NDIcm0RFVZjMsKddMbAK6PU02zfGKBFBnG8uqjKB4Ay0yQnlqwFE-AOZKp1JK3BXrTvVdsItNdyoiN88gNxpH1cD_rk1pQS4DvHHfXFCSRj0x4t2lotC035MDdnwUDDuJIuaJrlgFXrBK7gd6sjRlc1bJyYDjAbcmVjtTQMcij7GIyz7d2a1Cp2BFj0wwEn7tkdZdlf6E9Pf7E-aErHQffcLuvda8Yf7cumqLNsposcMWdV2Iw1lP9v5XIxijGlMVBF_i6TV5uoOwqadgzFIGRb0-JdFS6Gx3h49KjNgQqy1KdikmuKl-WMYCrw7G_KUD0jGR4E9xn_YKl8_YN_6PTSD72smloTKbpL1TzLg6fmWBKpnV6jAIRzczynhAgMt1QvIlJtBFWhxeihemegBlRwZljUSXhXeaGntv7CvOF91wX-oRDbnKE2wJj1A8CvohqbIN1aoM8OsLuzZkpBxXbdJalT6cqSqgOg7rLrIgIcOaQX2g16WPDjKTZ-wPlmOV_Hdu7WFpvgM0mdvgKDZGISVKSeFqmPjHmwP6-EhIR4XW0tHeuKVCXCbiH766-BnLrokBYJe98zKab-eIT6rzVZwfmnUV-RqD4DFLQETeetWFNgXtmrBgD6O_mqQkDMPp-hbVsmD1TljamndKUuwpl5Yt8QzzTatOFh9DKDPGd03Mb4ZtaeXGP-D502TgUk4Ndco99UbYSHsnE8IInJiDfRKyXXZEcUJUjuoLXooASetytdVE69Wrxnr7Qwy3Wpe9oOOmoa01asPUDWtw7II-nf1SqRlmDGDvDwOWAMj0X8niXjV6EOECnAIGD1oW9ClXCrX5LAMdB0qqa_d061pfXcDXvmVRpfaboAHTHETaqqUxWpXBDhA8myOzFshIjEc1LpZJtqzx1gwKjivmzug1H2o5kTyXST8K4gO7oLcC60moJ5KtKTX672AxU1REVsJVYUbFRe48iBeX64rorIiHCf7OFYqM6UpUXh43UuL8lcPi4eV0H9mjDqojM3ijbkNB8MPipVFp7pv4tYNcyJ7OKWkeye0qyDQLm0uaBEQk-zXabsE6DLW6IAquE3I-DFXPerElrO91p84ON3PUA34TARTfdtW95fKveMnHKLCOyon9rqFVgsgMi4978uAcEDNlMiaFRiyJtti22mvO1vhZBxJRVeDHNWOibtu_rF_S5zW8D4Z5CbG-q8RJnzSUvoLhic7RyeKkiGs3Ezb81NhLudpmSaq8ub5kDsIT7l7Y2XPycck8t1WrPh5TlwiDJgcpiK-SzT3ZBkM4DWcwQJrC7Q1WjRXWYOTPJzsGWORIv73ampnmlCGKUCpi26aSoDUD0iHttOsJzzKSJ18AH-5HQfBPBpVF_aZfMNWTQOxO3jExUo1xgrBI3_PPBuAEEAv9Lsa55uQpOqw2yiumfpjtx1Z1zVxzIevGVpu_dG8aa0kAS2opUflybzzZZ_i00gY55aIdaQocMEeXT2LcsHi7bUoahSLY1QK8mmbrsuKwLVvyuaEwz0HvGtKDUyDDBne9vGsitR1hOpugcadcsKLSMenaSdEKkAj3d-NGXFSoA6m29r3-vNGqnAqiC_oaJO1XkjWhRGv1E5qaWxcEN5bTMZCHJnXZdaorwFH_aGDeoi2lTqWVeri0G_NHHghoLAcJlhotzkTpStCq9m--CpBZW3YhXdy__QsqVof7ZOsOj6kwT2q1lTXuzyCFS8SQ2qrBBaYZVaqszBcPY7J0JNiL8WI2Jf5EqVqgKg7vroYIEU9OXcXY932HPg4HU5wPWiOJ_OPaFWFNnpdEiZvQYKIKIZmiUeXOJHgDm-uCaDxgp8lWVqUOILVCpB5uGybCYLUPQiHh-I_xv_Z649f8I5r3haCnIuldG",
                  "width": 170,
                  "height": 170,
                  "precision": 1
                },
                "touchPlace": {
                  "url": "https://avatars.mds.yandex.net/get-afishanew/35821/0f0465b1d24e2d04995ebe9be0a8ff59/80x80_noncrop",
                  "width": 80,
                  "height": 80,
                  "precision": 1
                },
                "touchPlaceCard": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_47mlk0AgYVedTnGWcudl92ie6SxkjQ645FLTk6oyQJ43RAylqRPbKpRcYQxBMb8z4QaNxb7frumcYAJY5citJnuhaI5V-axQlQU6Gf1oq_P4SDFmvVIBd62RXhEsMwMdegtHZ6mRkiKd2mMETfqz--rGRs0z0qxo3SEFnWYG7Cd36OENnbIm3ttJ-9jyY-e3uc63Yf1UR3MvW5PW63ZHGbTMj2Ng254hVF0rjkGwcbAgSM_MelKt7VNtz1ypxW-tvCGtBNG3K9USQHmccW4iNPiKt6m8m8G-LthfWew-jdd9Co9vaxBXqFfVpM0DMjuwIAxFS_yUpWhWqAzUq0QtI_IproWQ8C0dnQn3FL0npjG1iPZkMVLOP-pYn5vrssnau0JPbaGYWmyfGeTIjnf5uCCCREr4lmXs0uHK3-1EJS834KZFFvhrHZOFe1_wYaYxfMD2IHtRwjlqHhJRbvQBUjQGwSIqk5yt1JnrSEz2fH5pDAZJv97soJpmDFHlheCqt2vuR18wYNUSjzfbfGkpdDhGNKm5EA0y6R6f36O-wpVxRAXnbFTRbZcRJsiJMbQwpoNKwP_aryOd5I-R5IvpaPpp74bZ-irdkgjxET-obvs6w7Cost8P_yRSk5hh9Y0d9clK4mufFGBf0qnIzj05P-8EhAF93abpmupNmKSEb60-4ehNXXpmVd0E_xS6o-L2OQ35qTJbBDihm9ta7HlKlXwOy6bolhHg3tFgxw469H7qRglPNlUqZFXhCtsuxWXiMqhtC1ZwrB_fi3GTsyJhP3oLfWUynETxZ5TY1mo9ydx1BcVgItvSpd_XaMSDMPc26UPMCzTTq21aao1ZYYtlYXUmK0FQv6RXG0z0XvgmavY6iXjqv5bCNmISm1ugdQCRtksIL6CW3GddGKzDCbI5sW0JCsK81GKnmu3LEiSD7Og6JmfJWPhi1VjMPR-0Ki66_AG6Z7-ZjjiuG9UWZfdK0jRCBachF50oF9_qRIux-PqtQodE_99pb5WkQhQhA2So-iDpCxyx6l7SR_LTsGdr-zZMNSk5WIDyrVoWH-zyQJE5yIQoqZsWZd4XqUzP83Fz7UaEi3UcoeBUagvd4IpuI_ukJ8wXd6IRGstw1_guqbQ4CDcmsBoOci1YU5ioeoIZdg5JL-ien2CVFuqHD_u-964Kjcv31apsnaTOnO4KJqe1pmcKmLZs3lPL_VR4reUz9Aw2oXPQgborHFBRpHyElj-JACWgk9XpnxAkBMCxuTNuxY9Ce1YhqphiCtSoyOrn82viClj5q1jchXwXfW5vfPLKeaT0GEawYRuWmeX5g5f-DsHoa1PZYB1abMeNPrbw70hJwPwea28SqYOQoYZgr38pqkqYPOxfHcjy0XqgJv62S_Ak_J6I8GNT31fq_0tV8sKM4qSQliucGqHAhDY_eaGKRIJ1XOpqUizFXWrJbmn_7ONOlLQin12BPZdxZ6b8cMV8rjRTgfsk1h9bZPlIFH6NRethF9bgGtAkSce6__psDMVHsh4hYl6kwtzlBaLuMyciQ920qh0WTLxWteGuOvHMOe2wVwd_6ZPa0CW_xxayCszrplvV6B5QLI9Iv_4_ZELHjPrVZOucqoKQ5sina_DlI8oYMeMc3Q59HLgpI721RLDkcBOFd2QSnBqlOklRso1JKuESXaUe2OAPj397v67OiMc7Fa7qkmQIVyUK7Wa77SYFH3SoHp8DshC44KaxuMu6JDwZxDNu2J0foTQImPWDgesiWlphWZ9hD8V2MLklRAjEsxTt7BwhixugBGni_C8lxdD_b1kUzT1QdGYotrwJPih638r_qV1X0OJ-hZf_SMSv4hGSZNhdIgtD8Xa-LIIODP0fa2Bd7QecLcrt7jLmJsVbNO7elsW_WHMoKr9xzjgk8xjCfSMQmJ7jvc-WtAuCJGyeVitYEGBPQzk_O-FBQko3XmnjV64Ok22K4iM2JK9GGHak0hJJeNa0Ki-9OUv94rPQBTGjmVQa5TpBn_GMAG5tXtukHxqtDo76_3vnBA9A9lMmo1wgCxgphafhNiOvzRe3bl0SR7tbOGJq_zfCf2D8nE7_pN5bWCW1Qdk6TUAjLl4ba1SfJMMOd7By5oyFh3_VbqUf602TIIPqIvpgYA6WvaSREw551zGoJjnxCblgsVQPcWGUmpnq_oPds4mJp6EX0ede32POTvd3960MjUT022RnV-UAmKzMJOF3piBEFLSo3xeB8Jsxbi759kPyL3lQgvUj29OTojxNHf-FyO6qEdPi3ZJkCU8zvrlpS4_POhMuItKmyNjmzioodKmjyhB-rZlTwPvQcaBvtj_Osq7yXE875dYaFmu2QZkzgQzq5F_eqZddZEnB-bAypUaOiLrc7GgVYgeQKUFo6Pepp8sXdqIRUsgyVPDj6H-_ijqmMxnHMWpYX1ypuotSOY5LbeHZnmSWEmPDz_Bwdi5AxgP7laTrFKOMEurCLuD4r-YKlzXkHhpMdN604y-9_Y2yZb-eiXksWpG",
                  "width": 140,
                  "height": 140,
                  "precision": 1
                },
                "touchPlaceCover": {
                  "url": "https://avatars.mds.yandex.net/get-afishanew/35821/0f0465b1d24e2d04995ebe9be0a8ff59/220x220_noncrop",
                  "width": 220,
                  "height": 220,
                  "precision": 1
                },
                "touchConcertPlace": {
                  "url": "https://afisha.yandex.ru/q2a571P07/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-vYLulkQMyrgAI2PGHpmmofL5N_aZ8m8ZzI1XVU2HzypS3icBiotBWLNpVJAWNMjUwrIyFjLbWaiwSK0eZZYKo4D5m6Ite_KqQ3gC7XnlmZzV9wH8gfdhFPmweF1PjusKdMYvIbmncnicaniyIgDC0ce2LQA94l2sgW6LEUS4IJq5ypymEVbDu0ViGvB5_IGO3tw245zicQfCr1hOaqbbBVLbDQmIjHtXtlBctwQAxMf-hQYHAuxTh65LuzR0rBS1neyVtB1h1bZAchnRfsKautjTBN-BwVo85bdYfkWJ_SFc-TAEgoVTV7dCdqkfGObT6ZIIJwjpWb6Wa7UxcbAPl6DKr5csR8WjdHse50nmpL3K0AfXn_BKC_yUWHVvqcoyf8gwEreSW3e1enKtDxPkwfi1EAoQ6XmNgU-WM2mRF5ea-J66GV_FoFFbH_Zh6pSny8ow_YrraCnBhmFLQ4bRN1HIDhG9lExuk0N6oBIxwfDaqgoyM-5vm4NitjpOsTi1ntGsqCl9-LVDQBXRaO2oicfIBsa_wGc01I1yXlib5jZf6zgSqottVa1-SIUSIM_8xKAFMjfWSJK3arE8VZgQl5zOt4EmeOaJSVYF1UfRo77y-DfZtu1ZFsa4TkpHtPIBfOUEE7a5WWiLYXODGjzo1NibDRc36FOFpUquEkeZIrag_o-XMlbWvUZvIdNFwYyg5d0U04DeRzThpktYS5DkA3jqICy2pmxsnmtGujQe2uPkthAZHux6uZRsuwprsgueqsC1ixRQ2ZhKdTLjRtyPh_3hGuGZzEoQxYpwQ2Kn6Rd88gAigo5hTJJ8U6o-BN7H2pgOECPUeLSKVaIicI4qvbneor44QPa9SH0k3XL2lJvr-BTWsO9vJ8ixRX1rk9Idd80QPKiFW1KDV0iMHhv57NiFFz039l6RtlSQAlGRMLS33Ye7CHHnjlJeLulyy6Sg290t4abmRinAlXNfbZbXIFzQCiKgil59gnl-lRI31szlozMlIfR_krZOqwtAtxKanfK4ixlE8ol7aBPTac-fiNbaIceC8m8l9r91YU-k-hd78QYDsYB4WIJpcas5OPTz4poUAifQVb6wXZAXb64zpb_AsJo4Y_u1Qngb7UzFpYrW0zfakNFlBMmkQXxLst4CV_QJLLGjRkmPWVSpMhzawMWhAQYd0XeviFSTDVCpCJibwoaUOm7JqnJoHfJD75qqz8M4_qDJfznvuWVVa4f0Jn_vMyOMi1lajGVejwAS9djSuhAnBtpGrpNihw5RlhaCpviDmC1g4JZpcSHkXMyGg-fcI9-m3WM-6aZiYkSHxgB2xhAuurdmVIpSRIUdM97O-ZQ1NyPgb4yia6YNUoMKnaPOuIAyWcafe3cH5H7Xv4Pu_QTnmsZANtqXVkl7ivsuc8UkMp6VQHGxWnGPODna2_uBLgAO3FSWoX6CHWCgMZyi6YWYHUfGlGFNNc9d45uu8OoE1aLeTTDrqHJubZf4AGjvMheQpkJ-h0B2mCUy9vvJoTAGMe9miZJRhihEohOVjd-Cnw9f5Y5laCDBTfGBvcX9EvinxHE72bZWbXCn9CB67xENrLJFaqZ4fbUGH-DcwZgxNj7bcJ6dWYAPUrc3kqDUh7c4fdOTd0oE5kzjiZ_z-AnSpdJIJ9uoQWhtgdUUeMwjDrOwU2mMSUCaARzI2PqiGikx0lirsXmXM0-iG5uo47uHO1vHo0F2L-d8yoyP2NANxrXrTwLHk2JvYKHKBWXSJw-blX9zomNAlCEZxMLDtBcbJehKuq5xmDBxjQaFh9mGhAlB_79SfD_WZ9K3vMbHJvu4wXs-7L53fGGO6hNi2ysdgYhnb4V7W7UZN97zxIYlBRLSWomVVZQyXqMAm4_7jqQUefeYZWAn5EDOlbbv8BvDv8xTO8GzbVJbsfstY-4iDYKpQXiydmquMDPU_-2KATgT0mW9hl-yP1OqKKmdyJCfCHHjkUd3MP1D7YiE7dcp06XSax7XrWR6XLPNEH_FFwq1pkB4q2NehTQG6f_DshcVA-9ytYZDsBNsrQKVnfOeqTlQ9pl9UTr0ftynvPDLFNin7moF-KhlT1Cwzi1R0zA8t5N8XK1BdZsSH8nmzJ8NOSf2Rbq3TI8daIYppZjUlJkeecWCZn4i9Un9oYfl4BPfmsFiF9-7Q11tl-QdeNIsCbWQYkmDQVaVPifi7-ymORcWyX60gFWON2CiGJ2K6rGpHWHmgntXD8pp75eW7N039rnKWRbvikZ5QY_sC3XmMxWyg0dykl1cugUGy_n5qRgWPsFFkIxrgA9zig2Em-6chB5Y471dYg3MRdygrfTqEeGf4msF35lWaHi32SZe2jIXiat9XaJpWaQGOcLS5rolNQD8TpKAa5ALb6ozpJ_NupYbVvybXHAt70DKgIfK0wTKl9FAKfekSHRurtoSW-YsP7GMfE-OcHuJAxzg3uG8Cz4O8VayvHKXDW6nK5m93KC_C1XjklRuDuFy17mm0tg0_5TGURfIq10",
                  "width": 88,
                  "height": 88,
                  "precision": 1
                }
              },
              "address": "Комсомольский просп., 28",
              "type": {
                "id": "5575d419cc1c724f5a8e1125",
                "rubricUrl": "/moscow/concert_hall",
                "code": "concert_hall",
                "type": "place",
                "status": "approved",
                "name": "Концертный зал",
                "namePlural": "концертные залы",
                "nameAcc": "в концертный зал",
                "nameGen": null,
                "nameAdj": null,
                "plural": null,
                "rubricPlacesUrl": "/moscow/concert_hall/places"
              },
              "tags": [
                {
                  "id": "5575d419cc1c724f5a8e1125",
                  "rubricUrl": "/moscow/concert_hall",
                  "code": "concert_hall",
                  "type": "place",
                  "status": "approved",
                  "name": "Концертный зал",
                  "namePlural": "концертные залы",
                  "nameAcc": "в концертный зал",
                  "nameGen": null,
                  "nameAdj": null,
                  "plural": null,
                  "rubricPlacesUrl": "/moscow/concert_hall/places"
                },
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
                  "code": "concert_hall"
                },
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
                  "name": "Фрунзенская",
                  "colors": [
                    "#cc0000"
                  ]
                },
                {
                  "name": "Спортивная",
                  "colors": [
                    "#cc0000"
                  ]
                },
                {
                  "name": "Парк культуры",
                  "colors": [
                    "#7f0000"
                  ]
                }
              ],
              "coordinates": {
                "longitude": 37.57964499999999,
                "latitude": 55.726876999999995
              },
              "bgColor": "#4b4b75",
              "logoColor": "#7c7cc2",
              "distance": null,
              "isFavorite": false
            },
            "headliners": {
              "title": null,
              "description": null
            },
            "session": {
              "date": "2118-11-11",
              "datetime": "2118-11-11T18:00:00",
              "ticket": {
                "id": "ODQ2fDk3MTM3fDEzMjg2MHwxNTQxOTQ4NDAwMDAw",
                "price": {
                  "currency": "rub",
                  "min": 140000,
                  "max": 480000
                },
                "discountPercents": []
              },
              "hall": null
            }
          }
        ]
      },
      {
        "date": "2118-11-13",
        "sessions": [
          {
            "place": {
              "id": "5516a4171f7d154a12dc66a1",
              "url": "/moscow/theatre/places/mdm-5516a4171f7d154a12dc66a1",
              "title": "МДМ",
              "logo": {
                "bgColor": "#4d4d4d",
                "microdata": {
                  "url": "https://afisha.yandex.ru/q2a568P13/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-oci_iQdWgeMEeWKYYOmgh8r0CcW0z2sg2bJFX3ut3gV2-zMPkqZ8RaBhc6AxNOb3-rY2MAHPaKyoXoIMbbMvkoP2h6E_RMK4ZVIF5F_Uh4n8_hHAusJeHfa6R1ZfjfgdftsAI6GGU0aMQ0eUOzHj8-WgOQkFy1mKjlGjIkeKFqGE8ruMDlXEon1PBf1Hxoyiy-EM1arRZQLWqWJ-b4LeAFzzMQioqXl8qEZhlD0n2sDOpwYHC-B2r750kzZzpTKHjeC3uxhYwbJ-bgLDXPKKrfndEfaB6kIa1plNUUmm0CJh_jsBgKl4boJYeowfM83XwIcMAgHZTo-wcZYqaIcPobfDhp0ITfW7eVg152L1mK761Q_Hkd1bOdaSZ3F-tfMTYegOFoiJelaGXGqHHSHc8NiqFAIh6lmrk3OOC3CHNZOG7rOFCE7Qm3hJHetS75m0zf8a3LP_ZivvrEteZbDdE1_rBBCfkFxvjlF3pTgQ_u_CkjcFN_xbhrN6qStfpTG6tPyDpzVbwoBybhTsbsGVtvvEL_e84nMg_LlQQ1Kx0zBp6BMPvqtiUrx0d7Q2HODlzZIzPRD1b460fLICd4czpa_VjKIrZ8iWYmo70GX2oIbK2ybagsBhFcCtT2xGhvA-VekPPYqWRE2Hcn-oETT83sW3MwML4n2uq1KgA0WmD5WXw5iMG1PHr0ZsOcBK6Lej6dEQ6ZziRgvFv0NIUIT0MXHWDyK_klFHsktRiiMDwPPYuRoHIt5MiL5KjChsjgWrrd--ihR2y7VVXDrdSc-vn-fjCfuRxmIn_qRqf12Q8ClR2DsKsrJdUKdbW5AnJ_7dxrAnPyDTUrGnYpcUTa0Wtbrqkpo7U8m9Q2IO91LTuYbp1CDYtPFvHMuaY0tmmvsWQcYRAYisTHu8fXuPAAz8wN-dMx0G9m6wlUK2C1ekGLaf76KrKmDTnklWDspi6Imj0OM20Z3_Zzj9uGVOY6fQC1vYGQ6Ng01VimR3oy8sweb7hSUfJ_Vuqq5Lpy11ijKZoN-znj9n-qh0bBXOWcCEpNzFEsW081ES-4ZHfE6Q9ypX-QgEq6ZNRYVaXKwNE8bf3KIjOw3ZaLmVV4g0VLUQq6jOkrk2W8O4fFIwxGPChK3K2ADmvtJuCc-bQ2pqhdsvWNYIJ5W3QHWgWFeIIyDh5MmmGTovyFCwlk23M2-INKmewJC0BETzqHpNP-5c4p29xfww_qTvSBTrsmNfQKHzNGLZNQ-KpENJqn5lhgw49v_YhwIxHslLhoJOtgxxkgmTm8yHui146LFGWyDNQMu1ot7dNuq46E4L7IVMX3KH-h1B1AMztapFfrB0eKcnLt3R_ZcnCzfreo-jTbUZbY0MpaDUmIMLcfq3YFsC1nnLvIP55Qrxm-B9Otiuc1JPqf8edcgnEZOPfnaFfl2tIzvfxOagCjcM8Xmah12HOlaMDYKdzLedC3rgjVJwIeJd5qKU-dcy6ZbmTAX8iWVPTIfkNGPtKSKRgEhsgmlApg8b7eT4pjUEPu5KtYNoozh0hSK0msulhShg5KhHfjHwR_WXg-_6N_Oq7X4b2Ip4f0Cn9jRA9xU2lpRpVIlEY4sZPOXd-ZY6MCj5Rb2FT7UtUIIPv5_jkqceffaKY1kw4k_XoYb00DXlk_F8Bc-PZVlhk_QXcvQKNICXQ2W0a2SIMTje59KJNTkAzGmdknOoOHyLB4ij05GBCk3AtkhYAMtKx4qu8MQl3JTUYD7siGh5foLpCXb1IhGsjW1PtGVEjT0i5_HfuyEDEt12lZ1wlhdhlSiyntCjmzJR07xYaRvTcfSUudv5KPag6EsT-ZtpVl6U7gB65zgMtJFKV69EfKMnE-DD7aUWOQLuTbGRcrk5Z4sgkJbwvqM6duSgQFs8z1P-vY7mwS_7iO1mHuO1U2lPqu81c_c7LZKGfVqeX1WnLR_Jz8mYFzk92l67t3-0ME-5MqOIy6KrLn_Gt1dCP-xOzL-p1NE15bDIcADqnVRreZfzHkbwDCKThmRPqnRRkhAf5_fftQcEKtJep7VTizdlhTKYhv2Tijt3_JFdSwLdYfSitenaN9mx018F66hYaHqq3Qhhxg4Xr6JibYFqd4swBujaxZkjHR3db6iKXY8cTrU3v4zNtKMIbOe-RUo1_GfPt57u3Qr2ucF4Fs26ZU9QmvQJffMMFLG3TG2iZFuzGw_I4_G3EiIm01ixi3eHOH-NJYGp_be7K2z6l2h1Fe5R3r6jyvQp_YLASCfInklXWIz5PWLvCweUjF1xqEtgkjIZ3ezQtjoqHfdUj4VPlBBqlDSFhNC0gi5T3KJqczndZuWmlOzjD9Ww03g02I9wb22h0gFj7TAvrqNtRa1VY607MsL_7ZUEFxb1WI-VS4gwVLQwpqLCsYwxdd2wSlA8y0bPmK35yAfmm_9QCcaTZnZuldc9fcUICK-xQVyPeGaIGT7F-cOeChoO1WSWkk2JPUyJEre466GPLnzVrmleDtZ_7oCmyf0E8YrBbwbT",
                  "width": 960,
                  "height": 960,
                  "precision": 1
                },
                "place": {
                  "url": "https://afisha.yandex.ru/q2a570P09/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj--Yqu2UxP0-oJLjSQFu-godTnJNuHwWET_6tOXkyw0iZx2QU3sqtMaJ5XYoE3Ms78yYEFJSf9a6u3V6Q4UaoTn433mr8zd8GpUk8f92rQnYba0S7Dgs9sJsKERlxFlPIAadElBJ6YbEede0C1AzjL-c2eEyoe-W-akXGrGX-AKqa-8J6DHkbQr0hXAvdzyI-N8eYx3pfffx3dpFV5baT9JnTzDTW1kUNtp19FkwM-3cD-tRQVEPdEtbRBjilrtAWCmPmMjylQ3apYVCPwTdO7i_7UDcO09EQ6xaRlVkKC2ShWzgA_vLlDbLV1W4gbHMnX6bs0HxX9fY2UT4ssd68nv77Dr74PQMieUVMVx2ntvJn91wXdheRzI-akbnxitcoLZ84WCquxY26NcV-YEB7bxs6jGQcV3U6asGyJNFa3J4WM8oKLF0DLu3FSBO9l3aaY5-AvyJ7GUR70nVBQTa7PJWfwFQCtpnpItHlShTI76uTRuSEkEstYmJ1MgBN2mAWBpcCQuzV93qlqWCPmYuGIlOXWFP21yUwL_45FS1CZzitExhYXsodBdolLd4UjNeb627YhICrsUayVS4YIX7Ang7rbubQwY-KjfEgnyV7qv6HV5wv0mPduGcqyUVR_jfkISvoXC4CzfFCWcHGNPxLO5uC-BCAU90a-tVSoGl6CBr-K46-gHlPWrEVsIctOxaG28MQBwqvpTD7Ut0NYW5v7DEXeKAufhnhFnEVIox0g-drNowoJEN56j5NBsDZ1qy61tNmzhhhc86BffxHIU8aGrszKM9u55Gga-IxYcWyW7whd_iY_t4tYSYtQWKkHJN3k470DNCjcd5GqWJgtSYoNpqrOhqoIc9aiV2kv_HndmrjVxATymsFfF8O5ZnhYreUDYu44FbyxRligS36JGAP25v6kLiAK-lKtq2q4DFaQBKip64OaOWLluHRjG_xE7aGI8P0z5JPoUR_nj0R-XajYKH_0Jh2ztGlZjn1nhTQs1tvYgDY2CNtRrbFRsR1wsiqChtSziwx34pFCXiHnQNaJhffxFcCHwV0pzYl6XG-F7w9e-AcMuZJMWZ5yWa47Dunc4acRMCzxfauiaq0yaZMVoLTcoqorft6oUlYfwkrsi4X-5wjSpMt8Fta9Z1h5ofojW_coDJqsXVSuV1ulHyDa-9qyFQot02yTq2m3DW6oKIS26qyoJkzBmEJQAM1g06uc7ugs4rzRQTDLmU54TIveC0DNJzGys05Xkl19lxEPwuzBozQRJuJtiJ19tAxRtjK5jO-gvyhl_YNbbBbSQ8-CtPHzDeSozUY21J55V0y5-AJp7ioHjoxAUaVHd4owJNTH74YkNBzLT7mUXLcPRKotvLrUuKARQ_SRXUoW8Fj2gr3Q1DXYs-5OBeWqUmhBhNYHato2I6yqZWqtcn2vOiDBxfqdExkg8FW6gXinPWeRLL2d6aCPD0P_i2d4PdNs0q-jx9QH4KvjSDTajnV-XIf4HEDMEy2fqGpct3VqsjEM4ffagxUmE8JKia58khllsyWSq-6nnRdg5Y9CbTPDfsi8ltDCKuWx30MGxKp2Y2yL2A5A7wkRi69-fY9-R5EcGsb_44IlKSfUXYamerUPcJciv6Drj6o1VvidYEkUwmzAnqDV2QDnp-ZfBNq9c35KquwMY90KDom5fVe-Q2iWHzLCxNmpOiYu_Giqhm2JEmW7K7eX17-pE0LIq1xiFfJFxY6L_d0U957hehjhnnRzarX9EX3ZCyaslWd5lENmtho-2P3PpAgyFO55tY5iiixKpjWYreq8mwl61LhWciTpXf69ler2Kfq01UYzzItnckWV6xZ01Rk8sY17XoxYR440JOn6_ZYWBS7-So6qbogDZKArkI_inIYxcvOPSmoWzkHct7zdyxH9uf1DHsGRSUh6hNUXQdwJP5CrbGmBaVynMC7l0_GyKwQuwX6doEiFDm2IGYK8_KeaOWb6rV19D81iwYW--vkB56fFZgjfmGFPeLLoC2rpDgifqmxwlF13owUT5f3JpAYUE9Z2nbxKqTFqoiWCh_KRqxhz8pd7dwbwU-69o-bECuWbxH0n2plUQ3ux1SV8zjgKqpZIdrZ2aYUcM_zy5L4qMArheayzdac1QYkVh6D4oYwxQOmMVG8Hx3LohrbNww3YtMxvAMm_Rn5cm-UMfdINCKmIXVi2VWepJBj10t2KBAE12nebqnSNPWW4LZWe3ZGPKWPpkX1COOdg3pe_8Ock-7_3bjD4umJSRJPzAUnNEQ-6rWZJql9IkgUx48fSqwUpPeFTl5R6tS5NrTSEmvC8jBBm1rdIQD7LU-msp8fBM92XxX0A66pza3ym3ip1zBM0kpdJeZ5aVpE6OMjYwZYmFwDqUZuUarEybZMUgLnWrokeefC2WmAdzkXJhpn-1BjVpO5RKNa0b31lpeovSdI7DLWWW1WHeHuUHxrE38e4LRkN8nGnjW23M2CLKaKozIeZHWb5vkRDE_xY8KeB9eQt1rP_bxfZoQ",
                  "width": 70,
                  "height": 70,
                  "precision": 1
                },
                "placeCover": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_4rmlk0EgYVedTnGWcudl92ie6SxkjQ645FLTk6oyQJ43RAylqRPbKpRcYQxBMb8z4QaNxb7frumcYAJY5citJnuhaI5V-axQlQU6Gf1oq_P4SDFmvVIBd62RXhEsMwMdegtHZ6mRkiKd2mMETfqz--rGRs0z0qxo3SEFnWYG7Cd36OENnbIm3ttJ-9jyY-e3uc63Yf1UR3MvW5PW63ZHGbTMj2Ng254hVF0rjkGwcbAgSM_MelKt7VNtz1ypxW-tvCGtBNG3K9USQHmccW4iNPiKt6m8m8G-LthfWew-jdd9Co9vaxBXqFfVpM0DMjuwIAxFS_yUpWhWqAzUq0QtI_IproWQ8C0dnQn3FL0npjG1iPZkMVLOP-pYn5vrssnau0JPbaGYWmyfGeTIjnf5uCCCREr4lmXs0uHK3-1EJS834KZFFvhrHZOFe1_wYaYxfMD2IHtRwjlqHhJRbvQBUjQGwSIqk5yt1JnrSEz2fH5pDAZJv97soJpmDFHlheCqt2vuR18wYNUSjzfbfGkpdDhGNKm5EA0y6R6f36O-wpVxRAXnbFTRbZcRJsiJMbQwpoNKwP_aryOd5I-R5IvpaPpp74bZ-irdkgjxET-obvs6w7Cost8P_yRSk5hh9Y0d9clK4mufFGBf0qnIzj05P-8EhAF93abpmupNmKSEb60-4ehNXXpmVd0E_xS6o-L2OQ35qTJbBDihm9ta7HlKlXwOy6bolhHg3tFgxw469H7qRglPNlUqZFXhCtsuxWXiMqhtC1ZwrB_fi3GTsyJhP3oLfWUynETxZ5TY1mo9ydx1BcVgItvSpd_XaMSDMPc26UPMCzTTq21aao1ZYYtlYXUmK0FQv6RXG0z0XvgmavY6iXjqv5bCNmISm1ugdQCRtksIL6CW3GddGKzDCbI5sW0JCsK81GKnmu3LEiSD7Og6JmfJWPhi1VjMPR-0Ki66_AG6Z7-ZjjiuG9UWZfdK0jRCBachF50oF9_qRIux-PqtQodE_99pb5WkQhQhA2So-iDpCxyx6l7SR_LTsGdr-zZMNSk5WIDyrVoWH-zyQJE5yIQoqZsWZd4XqUzP83Fz7UaEi3UcoeBUagvd4IpuI_ukJ8wXd6IRGstw1_guqbQ4CDcmsBoOci1YU5ioeoIZdg5JL-ien2CVFuqHD_u-964Kjcv31apsnaTOnO4KJqe1pmcKmLZs3lPL_VR4reUz9Aw2oXPQgborHFBRpHyElj-JACWgk9XpnxAkBMCxuTNuxY9Ce1YhqphiCtSoyOrn82viClj5q1jchXwXfW5vfPLKeaT0GEawYRuWmeX5g5f-DsHoa1PZYB1abMeNPrbw70hJwPwea28SqYOQoYZgr38pqkqYPOxfHcjy0XqgJv62S_Ak_J6I8GNT31fq_0tV8sKM4qSQliucGqHAhDY_eaGKRIJ1XOpqUizFXWrJbmn_7ONOlLQin12BPZdxZ6b8cMV8rjRTgfsk1h9bZPlIFH6NRethF9bgGtAkSce6__psDMVHsh4hYl6kwtzlBaLuMyciQ920qh0WTLxWteGuOvHMOe2wVwd_6ZPa0CW_xxayCszrplvV6B5QLI9Iv_4_ZELHjPrVZOucqoKQ5sina_DlI8oYMeMc3Q59HLgpI721RLDkcBOFd2QSnBqlOklRso1JKuESXaUe2OAPj397v67OiMc7Fa7qkmQIVyUK7Wa77SYFH3SoHp8DshC44KaxuMu6JDwZxDNu2J0foTQImPWDgesiWlphWZ9hD8V2MLklRAjEsxTt7BwhixugBGni_C8lxdD_b1kUzT1QdGYotrwJPih638r_qV1X0OJ-hZf_SMSv4hGSZNhdIgtD8Xa-LIIODP0fa2Bd7QecLcrt7jLmJsVbNO7elsW_WHMoKr9xzjgk8xjCfSMQmJ7jvc-WtAuCJGyeVitYEGBPQzk_O-FBQko3XmnjV64Ok22K4iM2JK9GGHak0hJJeNa0Ki-9OUv94rPQBTGjmVQa5TpBn_GMAG5tXtukHxqtDo76_3vnBA9A9lMmo1wgCxgphafhNiOvzRe3bl0SR7tbOGJq_zfCf2D8nE7_pN5bWCW1Qdk6TUAjLl4ba1SfJMMOd7By5oyFh3_VbqUf602TIIPqIvpgYA6WvaSREw551zGoJjnxCblgsVQPcWGUmpnq_oPds4mJp6EX0ede32POTvd3960MjUT022RnV-UAmKzMJOF3piBEFLSo3xeB8Jsxbi759kPyL3lQgvUj29OTojxNHf-FyO6qEdPi3ZJkCU8zvrlpS4_POhMuItKmyNjmzioodKmjyhB-rZlTwPvQcaBvtj_Osq7yXE875dYaFmu2QZkzgQzq5F_eqZddZEnB-bAypUaOiLrc7GgVYgeQKUFo6Pepp8sXdqIRUsgyVPDj6H-_ijqmMxnHMWpYX1ypuotSOY5LbeHZnmSWEmPDz_Bwdi5AxgP7laTrFKOMEurCLuD4r-YKlzXkHhpMdN604y-9_Y2yZb-eiXksWpG",
                  "width": 100,
                  "height": 100,
                  "precision": 1
                },
                "placeCoverXS": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_4rllk0EgqFSKm6RSJHQp_LfKeW07FwXxr5xTEaG-Dde_SAjvLNhVYNEaqYHFc7S6rkBIQHOf5qzT7IXQ6I2urz0laMwZf6ZQGk18GP2rJjP-CfTvvRZGcuLTGNOhPETfts4K5yATWaja2mKJSH62O-8BT4XwUaet36UMUyDGJCFzaakNFnTqFFvL-h-9rWA3fMM5KHpTAnYsFNDXaHZI3H9JQm0sWZvjEFTriAH-t75hTYVEP5IkJxRsQFpswykqumArSZV5L5caj_rX_GLm-n1A9ad9G8i45dLQ22O9gVV8wc0ubtvR4xAQYQ-HOL87ZIhGzD0TZqlaZEPbLYQv4jUppcFZMKuSV427GnGr6Xu5wDVlepeMtSOaENmpNYyRtA2NK-OeE-sQnmAOgzp_v-DBgMd7E26ln61LG6uMaeI7pSmKFHarkp7Fu147qOV9OYa4r__RRD2s3p6WIj5KUP-NgqshH5YtWRAiDcRy9vOoRkZJc9KrIB8mAxniRGIquq9lDph-JNfaQ3nX-ekqdrqGNSEym4f66ZxaU2T5B5C8BU8r5NheY5afboSEdrVwr8TFiXLcouJSJALYZI4oIjooo8Tbv2NY2Mb91vImKLt3yjlm8NDIcm0RFVZjMsKddMbAK6PU02zfGKBFBnG8uqjKB4Ay0yQnlqwFE-AOZKp1JK3BXrTvVdsItNdyoiN88gNxpH1cD_rk1pQS4DvHHfXFCSRj0x4t2lotC035MDdnwUDDuJIuaJrlgFXrBK7gd6sjRlc1bJyYDjAbcmVjtTQMcij7GIyz7d2a1Cp2BFj0wwEn7tkdZdlf6E9Pf7E-aErHQffcLuvda8Yf7cumqLNsposcMWdV2Iw1lP9v5XIxijGlMVBF_i6TV5uoOwqadgzFIGRb0-JdFS6Gx3h49KjNgQqy1KdikmuKl-WMYCrw7G_KUD0jGR4E9xn_YKl8_YN_6PTSD72smloTKbpL1TzLg6fmWBKpnV6jAIRzczynhAgMt1QvIlJtBFWhxeihemegBlRwZljUSXhXeaGntv7CvOF91wX-oRDbnKE2wJj1A8CvohqbIN1aoM8OsLuzZkpBxXbdJalT6cqSqgOg7rLrIgIcOaQX2g16WPDjKTZ-wPlmOV_Hdu7WFpvgM0mdvgKDZGISVKSeFqmPjHmwP6-EhIR4XW0tHeuKVCXCbiH766-BnLrokBYJe98zKab-eIT6rzVZwfmnUV-RqD4DFLQETeetWFNgXtmrBgD6O_mqQkDMPp-hbVsmD1TljamndKUuwpl5Yt8QzzTatOFh9DKDPGd03Mb4ZtaeXGP-D502TgUk4Ndco99UbYSHsnE8IInJiDfRKyXXZEcUJUjuoLXooASetytdVE69Wrxnr7Qwy3Wpe9oOOmoa01asPUDWtw7II-nf1SqRlmDGDvDwOWAMj0X8niXjV6EOECnAIGD1oW9ClXCrX5LAMdB0qqa_d061pfXcDXvmVRpfaboAHTHETaqqUxWpXBDhA8myOzFshIjEc1LpZJtqzx1gwKjivmzug1H2o5kTyXST8K4gO7oLcC60moJ5KtKTX672AxU1REVsJVYUbFRe48iBeX64rorIiHCf7OFYqM6UpUXh43UuL8lcPi4eV0H9mjDqojM3ijbkNB8MPipVFp7pv4tYNcyJ7OKWkeye0qyDQLm0uaBEQk-zXabsE6DLW6IAquE3I-DFXPerElrO91p84ON3PUA34TARTfdtW95fKveMnHKLCOyon9rqFVgsgMi4978uAcEDNlMiaFRiyJtti22mvO1vhZBxJRVeDHNWOibtu_rF_S5zW8D4Z5CbG-q8RJnzSUvoLhic7RyeKkiGs3Ezb81NhLudpmSaq8ub5kDsIT7l7Y2XPycck8t1WrPh5TlwiDJgcpiK-SzT3ZBkM4DWcwQJrC7Q1WjRXWYOTPJzsGWORIv73ampnmlCGKUCpi26aSoDUD0iHttOsJzzKSJ18AH-5HQfBPBpVF_aZfMNWTQOxO3jExUo1xgrBI3_PPBuAEEAv9Lsa55uQpOqw2yiumfpjtx1Z1zVxzIevGVpu_dG8aa0kAS2opUflybzzZZ_i00gY55aIdaQocMEeXT2LcsHi7bUoahSLY1QK8mmbrsuKwLVvyuaEwz0HvGtKDUyDDBne9vGsitR1hOpugcadcsKLSMenaSdEKkAj3d-NGXFSoA6m29r3-vNGqnAqiC_oaJO1XkjWhRGv1E5qaWxcEN5bTMZCHJnXZdaorwFH_aGDeoi2lTqWVeri0G_NHHghoLAcJlhotzkTpStCq9m--CpBZW3YhXdy__QsqVof7ZOsOj6kwT2q1lTXuzyCFS8SQ2qrBBaYZVaqszBcPY7J0JNiL8WI2Jf5EqVqgKg7vroYIEU9OXcXY932HPg4HU5wPWiOJ_OPaFWFNnpdEiZvQYKIKIZmiUeXOJHgDm-uCaDxgp8lWVqUOILVCpB5uGybCYLUPQiHh-I_xv_Z649f8I5r3haCnIuldG",
                  "width": 103,
                  "height": 103,
                  "precision": 1
                },
                "placeCoverM": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_43mlk0DgaFSKm6RSJHQp_LfKeW07FwXxr5xTEaG-Dde_SAjvLNhVYNEaqYHFc7S6rkBIQHOf5qzT7IXQ6I2urz0laMwZf6ZQGk18GP2rJjP-CfTvvRZGcuLTGNOhPETfts4K5yATWaja2mKJSH62O-8BT4XwUaet36UMUyDGJCFzaakNFnTqFFvL-h-9rWA3fMM5KHpTAnYsFNDXaHZI3H9JQm0sWZvjEFTriAH-t75hTYVEP5IkJxRsQFpswykqumArSZV5L5caj_rX_GLm-n1A9ad9G8i45dLQ22O9gVV8wc0ubtvR4xAQYQ-HOL87ZIhGzD0TZqlaZEPbLYQv4jUppcFZMKuSV427GnGr6Xu5wDVlepeMtSOaENmpNYyRtA2NK-OeE-sQnmAOgzp_v-DBgMd7E26ln61LG6uMaeI7pSmKFHarkp7Fu147qOV9OYa4r__RRD2s3p6WIj5KUP-NgqshH5YtWRAiDcRy9vOoRkZJc9KrIB8mAxniRGIquq9lDph-JNfaQ3nX-ekqdrqGNSEym4f66ZxaU2T5B5C8BU8r5NheY5afboSEdrVwr8TFiXLcouJSJALYZI4oIjooo8Tbv2NY2Mb91vImKLt3yjlm8NDIcm0RFVZjMsKddMbAK6PU02zfGKBFBnG8uqjKB4Ay0yQnlqwFE-AOZKp1JK3BXrTvVdsItNdyoiN88gNxpH1cD_rk1pQS4DvHHfXFCSRj0x4t2lotC035MDdnwUDDuJIuaJrlgFXrBK7gd6sjRlc1bJyYDjAbcmVjtTQMcij7GIyz7d2a1Cp2BFj0wwEn7tkdZdlf6E9Pf7E-aErHQffcLuvda8Yf7cumqLNsposcMWdV2Iw1lP9v5XIxijGlMVBF_i6TV5uoOwqadgzFIGRb0-JdFS6Gx3h49KjNgQqy1KdikmuKl-WMYCrw7G_KUD0jGR4E9xn_YKl8_YN_6PTSD72smloTKbpL1TzLg6fmWBKpnV6jAIRzczynhAgMt1QvIlJtBFWhxeihemegBlRwZljUSXhXeaGntv7CvOF91wX-oRDbnKE2wJj1A8CvohqbIN1aoM8OsLuzZkpBxXbdJalT6cqSqgOg7rLrIgIcOaQX2g16WPDjKTZ-wPlmOV_Hdu7WFpvgM0mdvgKDZGISVKSeFqmPjHmwP6-EhIR4XW0tHeuKVCXCbiH766-BnLrokBYJe98zKab-eIT6rzVZwfmnUV-RqD4DFLQETeetWFNgXtmrBgD6O_mqQkDMPp-hbVsmD1TljamndKUuwpl5Yt8QzzTatOFh9DKDPGd03Mb4ZtaeXGP-D502TgUk4Ndco99UbYSHsnE8IInJiDfRKyXXZEcUJUjuoLXooASetytdVE69Wrxnr7Qwy3Wpe9oOOmoa01asPUDWtw7II-nf1SqRlmDGDvDwOWAMj0X8niXjV6EOECnAIGD1oW9ClXCrX5LAMdB0qqa_d061pfXcDXvmVRpfaboAHTHETaqqUxWpXBDhA8myOzFshIjEc1LpZJtqzx1gwKjivmzug1H2o5kTyXST8K4gO7oLcC60moJ5KtKTX672AxU1REVsJVYUbFRe48iBeX64rorIiHCf7OFYqM6UpUXh43UuL8lcPi4eV0H9mjDqojM3ijbkNB8MPipVFp7pv4tYNcyJ7OKWkeye0qyDQLm0uaBEQk-zXabsE6DLW6IAquE3I-DFXPerElrO91p84ON3PUA34TARTfdtW95fKveMnHKLCOyon9rqFVgsgMi4978uAcEDNlMiaFRiyJtti22mvO1vhZBxJRVeDHNWOibtu_rF_S5zW8D4Z5CbG-q8RJnzSUvoLhic7RyeKkiGs3Ezb81NhLudpmSaq8ub5kDsIT7l7Y2XPycck8t1WrPh5TlwiDJgcpiK-SzT3ZBkM4DWcwQJrC7Q1WjRXWYOTPJzsGWORIv73ampnmlCGKUCpi26aSoDUD0iHttOsJzzKSJ18AH-5HQfBPBpVF_aZfMNWTQOxO3jExUo1xgrBI3_PPBuAEEAv9Lsa55uQpOqw2yiumfpjtx1Z1zVxzIevGVpu_dG8aa0kAS2opUflybzzZZ_i00gY55aIdaQocMEeXT2LcsHi7bUoahSLY1QK8mmbrsuKwLVvyuaEwz0HvGtKDUyDDBne9vGsitR1hOpugcadcsKLSMenaSdEKkAj3d-NGXFSoA6m29r3-vNGqnAqiC_oaJO1XkjWhRGv1E5qaWxcEN5bTMZCHJnXZdaorwFH_aGDeoi2lTqWVeri0G_NHHghoLAcJlhotzkTpStCq9m--CpBZW3YhXdy__QsqVof7ZOsOj6kwT2q1lTXuzyCFS8SQ2qrBBaYZVaqszBcPY7J0JNiL8WI2Jf5EqVqgKg7vroYIEU9OXcXY932HPg4HU5wPWiOJ_OPaFWFNnpdEiZvQYKIKIZmiUeXOJHgDm-uCaDxgp8lWVqUOILVCpB5uGybCYLUPQiHh-I_xv_Z649f8I5r3haCnIuldG",
                  "width": 170,
                  "height": 170,
                  "precision": 1
                },
                "touchPlace": {
                  "url": "https://afisha.yandex.ru/q2a570P09/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-9oqu1kxr37VeeSXKW9-P3IamIaXv7EQ8xalGcH2F9AZByC8gnJJlfYV1VJA_HOvB0pcSECbcfpWFSYQNRaQ2hZ32k40rX8OUc1cb9GTnnZ_dxwrCk9N5G8ufTGh4i_kzfOcnIpW2RVudfXSjEy_L7tG7MCQS1nuQgVaSAnygMrS70JysBXX6rUBQH8hJ1oyZx98XworLaxDgqFN1bZvqCGPHNAe9hkp9gF9ckjgm5MTrnzUCEtBtqbJ9lT1yrhmbnuC5nBFB1YlmWQ3EfsCBnNfcNsW00F8W75pvaE6w0S97xwQokqBuc6JiUZgxDuTF-bUrGQryeb6lc7U3d6Qgo77uvJkNWve0QGMu9VjQlKje2wDykO5YBOyZZ3Z_oOY2WMcPArKXfVCTYketJgbEx8GxLwkB8GuvgmuYL3eEE7Sazb6BLEL3jnJSA8BA0JeN_toR2pzeQgX2rk1jZILEC0r-MS6djHh-k1xEpyAR3eH4uSIUI9VajZ1xoAxwkgW2t-23pgxt1YpbYBHwYu2Cn-XQNtOb4mwJ9Jh2Vk-N2R5B7SQ1gLt5cLBqR7A_MObfxYsHFDLbVpOXfqAISLUMgr_qsb0lRfeIRHs4_2fzvpXzwDL8p-lbPMSpaV9is_sMdNEwKq-vTlO-VkasDQTb-dqwARwu_H6PrHaFCHauG5Cf9Z-vJHfWtHRDLutJw4qayuQ0_rfGRSvhimNpUa3ZK2rUIiaLuUxXsXJ5rBIx3-zQhTgyDM5Js4FriyFyhyehueCHgw9e_r5KeTLNT8yvltD3BP2qxWIz3YRRcEOg_Q9G7zkPvLRYU6lSd5g6PP_gx5AoOBbKbY2vdYIcSoUqv4D5r5gzf92tVG4H4V_jipTY4TrJgN5-JcSKZllghcoCfdoHBoiPUliWQmmyMQbh8eyLDhgJ7UaPsmyvCGijD4OBy4-5LGXUo1dLAtFu8rmO--sOyb3uRRXhs1FPaazEClnsJQCNim9zi1h3uj4DzvDCvRcUJcJmspRItx5qggyDm_CGqApH-ol4dDLAW-e-p83WNNK51W0Y5r93a32FyDxz6hsiv6dYVKpUVqs0Jevw0rIpPyrgWbWtb5AYTqgghYjLmocTZsWrSnwj4Xzugp7d3gr3s-9vGO-panlej-kDaN4GJqmDTXivW3mrFxv6_eKXKzQOzmqSlnqUIk-KMb2ByIC4FF34j0hKLeNx3J2uzdgV-JnQTwH_pk5JRpXUJXX6LwacqWlQtGF2lj8E6f7enQ0GAOFyhY1rtTlEuzCmt9yDuStD4rJyTyH0f_WhtdTkA-e6zGYp4L1vT1KJ0yNq_RgpnJtPWZ1Ce6ADO-f46YcHGyHKZK6jTqUcfpISl779gLo-X_23RHQ560bTqKfSwgPFofVmIMGaV3NJqtsQW8kzFpGmYVyedmeEIR3Cw-GyDT4rznGstlWSMUKpCJSr2ZCIHWT8tmNJIcRY06O96PAo5pXRSz7WmmVLUafdIWTtFACMpU9HtGBCihIfzfX7tRojIOJRnpZLlA5xmxenhN2lrB9G9ZlVTibWQPC5uc3lJvaHy1gLwYxITkub1hN6yRcdvKlvVbRDWLYGGNnUw743AA30dpavSqQBRY0AqIzbgroKYvK0XksO4WLGpKvvwQH3lcN6PcSXYkxdosoRZN4SAJqIW1eXcVupBA7a_vKDGAcO3HKtlWG7DkylNYSszL6nH077vGl3PuJE0pSd0-oAx7zGahbsk3ZcZKXvDV_9FQ26l0pKiXVagSEiwNDYgxYnC9BolINsiRp2tySbpMO9mTBT5ZNTSj3QXuqIjtn6Mdyk_VkI-7hLUU6R0yZy6AYMlbdcTYB5SJs8Otz3wJg3HyXKWZOxXpctTKcXoIDPv7YeVfubcUIdzWbir7nF4gP7uN9TIcyFc1ZDudYLf_IoNqqmYky1cFiYHRzLwM2pLDYhwFW6vXqqLEyYI7OK6bK7F33JiUJcJtFu9qab0vUa-JvCYSPrt2NMXYHzHWH7ADGokF9QnkVfrxIdy9nYnQcyFP1VlIVshzxxjyuzluuehBBX9Yl5UhDgT-OuofT_E8Wq7Vk-94poTmGA6DJk-jU9q5Nifohiaa0nIe_f-rYZFA3dTJuodqsYaLgkgpnUkIA7fMWMXlggx2bQtbrb5xLyi-tiK9yNb3NOiPoVd9wnAIy5UleJflyvJD_68fqVFzg19kW7kUKFKVeDKrWA1bqIH039nmB9EMR-87Wn8sot0pndcyLhqUZQRbP7JUbZAyyUsURavWFAqDcaweDmnzgDFN9Trp5jhAFfuA65vtuCmzdY5I9kUD3HR_aKgcfIK_6q6kg61o9Rdm2B6BVVyRIVrIRpcYFgQpMfIO7Q0pomACvWeLGNXqc_YrMMtb7LhocXZsSLR3YvwknprIDV6Aj7vMpiBO-aen5eqsQ9aNcOA7WHXXS9fmqrOCH8_Mu4CwUO9HS2i3CsMW-rLImnzICGGn75qVZsBtJK9qWIy8sGyaHzQxzkoQ",
                  "width": 80,
                  "height": 80,
                  "precision": 1
                },
                "touchPlaceCard": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_47mlk0AgYVedTnGWcudl92ie6SxkjQ645FLTk6oyQJ43RAylqRPbKpRcYQxBMb8z4QaNxb7frumcYAJY5citJnuhaI5V-axQlQU6Gf1oq_P4SDFmvVIBd62RXhEsMwMdegtHZ6mRkiKd2mMETfqz--rGRs0z0qxo3SEFnWYG7Cd36OENnbIm3ttJ-9jyY-e3uc63Yf1UR3MvW5PW63ZHGbTMj2Ng254hVF0rjkGwcbAgSM_MelKt7VNtz1ypxW-tvCGtBNG3K9USQHmccW4iNPiKt6m8m8G-LthfWew-jdd9Co9vaxBXqFfVpM0DMjuwIAxFS_yUpWhWqAzUq0QtI_IproWQ8C0dnQn3FL0npjG1iPZkMVLOP-pYn5vrssnau0JPbaGYWmyfGeTIjnf5uCCCREr4lmXs0uHK3-1EJS834KZFFvhrHZOFe1_wYaYxfMD2IHtRwjlqHhJRbvQBUjQGwSIqk5yt1JnrSEz2fH5pDAZJv97soJpmDFHlheCqt2vuR18wYNUSjzfbfGkpdDhGNKm5EA0y6R6f36O-wpVxRAXnbFTRbZcRJsiJMbQwpoNKwP_aryOd5I-R5IvpaPpp74bZ-irdkgjxET-obvs6w7Cost8P_yRSk5hh9Y0d9clK4mufFGBf0qnIzj05P-8EhAF93abpmupNmKSEb60-4ehNXXpmVd0E_xS6o-L2OQ35qTJbBDihm9ta7HlKlXwOy6bolhHg3tFgxw469H7qRglPNlUqZFXhCtsuxWXiMqhtC1ZwrB_fi3GTsyJhP3oLfWUynETxZ5TY1mo9ydx1BcVgItvSpd_XaMSDMPc26UPMCzTTq21aao1ZYYtlYXUmK0FQv6RXG0z0XvgmavY6iXjqv5bCNmISm1ugdQCRtksIL6CW3GddGKzDCbI5sW0JCsK81GKnmu3LEiSD7Og6JmfJWPhi1VjMPR-0Ki66_AG6Z7-ZjjiuG9UWZfdK0jRCBachF50oF9_qRIux-PqtQodE_99pb5WkQhQhA2So-iDpCxyx6l7SR_LTsGdr-zZMNSk5WIDyrVoWH-zyQJE5yIQoqZsWZd4XqUzP83Fz7UaEi3UcoeBUagvd4IpuI_ukJ8wXd6IRGstw1_guqbQ4CDcmsBoOci1YU5ioeoIZdg5JL-ien2CVFuqHD_u-964Kjcv31apsnaTOnO4KJqe1pmcKmLZs3lPL_VR4reUz9Aw2oXPQgborHFBRpHyElj-JACWgk9XpnxAkBMCxuTNuxY9Ce1YhqphiCtSoyOrn82viClj5q1jchXwXfW5vfPLKeaT0GEawYRuWmeX5g5f-DsHoa1PZYB1abMeNPrbw70hJwPwea28SqYOQoYZgr38pqkqYPOxfHcjy0XqgJv62S_Ak_J6I8GNT31fq_0tV8sKM4qSQliucGqHAhDY_eaGKRIJ1XOpqUizFXWrJbmn_7ONOlLQin12BPZdxZ6b8cMV8rjRTgfsk1h9bZPlIFH6NRethF9bgGtAkSce6__psDMVHsh4hYl6kwtzlBaLuMyciQ920qh0WTLxWteGuOvHMOe2wVwd_6ZPa0CW_xxayCszrplvV6B5QLI9Iv_4_ZELHjPrVZOucqoKQ5sina_DlI8oYMeMc3Q59HLgpI721RLDkcBOFd2QSnBqlOklRso1JKuESXaUe2OAPj397v67OiMc7Fa7qkmQIVyUK7Wa77SYFH3SoHp8DshC44KaxuMu6JDwZxDNu2J0foTQImPWDgesiWlphWZ9hD8V2MLklRAjEsxTt7BwhixugBGni_C8lxdD_b1kUzT1QdGYotrwJPih638r_qV1X0OJ-hZf_SMSv4hGSZNhdIgtD8Xa-LIIODP0fa2Bd7QecLcrt7jLmJsVbNO7elsW_WHMoKr9xzjgk8xjCfSMQmJ7jvc-WtAuCJGyeVitYEGBPQzk_O-FBQko3XmnjV64Ok22K4iM2JK9GGHak0hJJeNa0Ki-9OUv94rPQBTGjmVQa5TpBn_GMAG5tXtukHxqtDo76_3vnBA9A9lMmo1wgCxgphafhNiOvzRe3bl0SR7tbOGJq_zfCf2D8nE7_pN5bWCW1Qdk6TUAjLl4ba1SfJMMOd7By5oyFh3_VbqUf602TIIPqIvpgYA6WvaSREw551zGoJjnxCblgsVQPcWGUmpnq_oPds4mJp6EX0ede32POTvd3960MjUT022RnV-UAmKzMJOF3piBEFLSo3xeB8Jsxbi759kPyL3lQgvUj29OTojxNHf-FyO6qEdPi3ZJkCU8zvrlpS4_POhMuItKmyNjmzioodKmjyhB-rZlTwPvQcaBvtj_Osq7yXE875dYaFmu2QZkzgQzq5F_eqZddZEnB-bAypUaOiLrc7GgVYgeQKUFo6Pepp8sXdqIRUsgyVPDj6H-_ijqmMxnHMWpYX1ypuotSOY5LbeHZnmSWEmPDz_Bwdi5AxgP7laTrFKOMEurCLuD4r-YKlzXkHhpMdN604y-9_Y2yZb-eiXksWpG",
                  "width": 140,
                  "height": 140,
                  "precision": 1
                },
                "touchPlaceCover": {
                  "url": "https://afisha.yandex.ru/q2a572P05/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-_Ijmlk4GgYVedTnGWcudl92ie6SxkjQ645FLTk6oyQJ43RAylqRPbKpRcYQxBMb8z4QaNxb7frumcYAJY5citJnuhaI5V-axQlQU6Gf1oq_P4SDFmvVIBd62RXhEsMwMdegtHZ6mRkiKd2mMETfqz--rGRs0z0qxo3SEFnWYG7Cd36OENnbIm3ttJ-9jyY-e3uc63Yf1UR3MvW5PW63ZHGbTMj2Ng254hVF0rjkGwcbAgSM_MelKt7VNtz1ypxW-tvCGtBNG3K9USQHmccW4iNPiKt6m8m8G-LthfWew-jdd9Co9vaxBXqFfVpM0DMjuwIAxFS_yUpWhWqAzUq0QtI_IproWQ8C0dnQn3FL0npjG1iPZkMVLOP-pYn5vrssnau0JPbaGYWmyfGeTIjnf5uCCCREr4lmXs0uHK3-1EJS834KZFFvhrHZOFe1_wYaYxfMD2IHtRwjlqHhJRbvQBUjQGwSIqk5yt1JnrSEz2fH5pDAZJv97soJpmDFHlheCqt2vuR18wYNUSjzfbfGkpdDhGNKm5EA0y6R6f36O-wpVxRAXnbFTRbZcRJsiJMbQwpoNKwP_aryOd5I-R5IvpaPpp74bZ-irdkgjxET-obvs6w7Cost8P_yRSk5hh9Y0d9clK4mufFGBf0qnIzj05P-8EhAF93abpmupNmKSEb60-4ehNXXpmVd0E_xS6o-L2OQ35qTJbBDihm9ta7HlKlXwOy6bolhHg3tFgxw469H7qRglPNlUqZFXhCtsuxWXiMqhtC1ZwrB_fi3GTsyJhP3oLfWUynETxZ5TY1mo9ydx1BcVgItvSpd_XaMSDMPc26UPMCzTTq21aao1ZYYtlYXUmK0FQv6RXG0z0XvgmavY6iXjqv5bCNmISm1ugdQCRtksIL6CW3GddGKzDCbI5sW0JCsK81GKnmu3LEiSD7Og6JmfJWPhi1VjMPR-0Ki66_AG6Z7-ZjjiuG9UWZfdK0jRCBachF50oF9_qRIux-PqtQodE_99pb5WkQhQhA2So-iDpCxyx6l7SR_LTsGdr-zZMNSk5WIDyrVoWH-zyQJE5yIQoqZsWZd4XqUzP83Fz7UaEi3UcoeBUagvd4IpuI_ukJ8wXd6IRGstw1_guqbQ4CDcmsBoOci1YU5ioeoIZdg5JL-ien2CVFuqHD_u-964Kjcv31apsnaTOnO4KJqe1pmcKmLZs3lPL_VR4reUz9Aw2oXPQgborHFBRpHyElj-JACWgk9XpnxAkBMCxuTNuxY9Ce1YhqphiCtSoyOrn82viClj5q1jchXwXfW5vfPLKeaT0GEawYRuWmeX5g5f-DsHoa1PZYB1abMeNPrbw70hJwPwea28SqYOQoYZgr38pqkqYPOxfHcjy0XqgJv62S_Ak_J6I8GNT31fq_0tV8sKM4qSQliucGqHAhDY_eaGKRIJ1XOpqUizFXWrJbmn_7ONOlLQin12BPZdxZ6b8cMV8rjRTgfsk1h9bZPlIFH6NRethF9bgGtAkSce6__psDMVHsh4hYl6kwtzlBaLuMyciQ920qh0WTLxWteGuOvHMOe2wVwd_6ZPa0CW_xxayCszrplvV6B5QLI9Iv_4_ZELHjPrVZOucqoKQ5sina_DlI8oYMeMc3Q59HLgpI721RLDkcBOFd2QSnBqlOklRso1JKuESXaUe2OAPj397v67OiMc7Fa7qkmQIVyUK7Wa77SYFH3SoHp8DshC44KaxuMu6JDwZxDNu2J0foTQImPWDgesiWlphWZ9hD8V2MLklRAjEsxTt7BwhixugBGni_C8lxdD_b1kUzT1QdGYotrwJPih638r_qV1X0OJ-hZf_SMSv4hGSZNhdIgtD8Xa-LIIODP0fa2Bd7QecLcrt7jLmJsVbNO7elsW_WHMoKr9xzjgk8xjCfSMQmJ7jvc-WtAuCJGyeVitYEGBPQzk_O-FBQko3XmnjV64Ok22K4iM2JK9GGHak0hJJeNa0Ki-9OUv94rPQBTGjmVQa5TpBn_GMAG5tXtukHxqtDo76_3vnBA9A9lMmo1wgCxgphafhNiOvzRe3bl0SR7tbOGJq_zfCf2D8nE7_pN5bWCW1Qdk6TUAjLl4ba1SfJMMOd7By5oyFh3_VbqUf602TIIPqIvpgYA6WvaSREw551zGoJjnxCblgsVQPcWGUmpnq_oPds4mJp6EX0ede32POTvd3960MjUT022RnV-UAmKzMJOF3piBEFLSo3xeB8Jsxbi759kPyL3lQgvUj29OTojxNHf-FyO6qEdPi3ZJkCU8zvrlpS4_POhMuItKmyNjmzioodKmjyhB-rZlTwPvQcaBvtj_Osq7yXE875dYaFmu2QZkzgQzq5F_eqZddZEnB-bAypUaOiLrc7GgVYgeQKUFo6Pepp8sXdqIRUsgyVPDj6H-_ijqmMxnHMWpYX1ypuotSOY5LbeHZnmSWEmPDz_Bwdi5AxgP7laTrFKOMEurCLuD4r-YKlzXkHhpMdN604y-9_Y2yZb-eiXksWpG",
                  "width": 220,
                  "height": 220,
                  "precision": 1
                },
                "touchConcertPlace": {
                  "url": "https://afisha.yandex.ru/q2a571P07/b094c5HQL/45tvpT1wF7l2LhWmSdWulEv-327iKGUyftFVueMJO0MCN2fsx-LPJbAaB7xUDGtKzVHaPdXPNoxpb1id10BFGuK-R5gURAaFemtR62T1g9Fj-vYLulkQMyrgAI2PGHpmmofL5N_aZ8m8ZzI1XVU2HzypS3icBiotBWLNpVJAWNMjUwrIyFjLbWaiwSK0eZZYKo4D5m6Ite_KqQ3gC7XnlmZzV9wH8gfdhFPmweF1PjusKdMYvIbmncnicaniyIgDC0ce2LQA94l2sgW6LEUS4IJq5ypymEVbDu0ViGvB5_IGO3tw245zicQfCr1hOaqbbBVLbDQmIjHtXtlBctwQAxMf-hQYHAuxTh65LuzR0rBS1neyVtB1h1bZAchnRfsKautjTBN-BwVo85bdYfkWJ_SFc-TAEgoVTV7dCdqkfGObT6ZIIJwjpWb6Wa7UxcbAPl6DKr5csR8WjdHse50nmpL3K0AfXn_BKC_yUWHVvqcoyf8gwEreSW3e1enKtDxPkwfi1EAoQ6XmNgU-WM2mRF5ea-J66GV_FoFFbH_Zh6pSny8ow_YrraCnBhmFLQ4bRN1HIDhG9lExuk0N6oBIxwfDaqgoyM-5vm4NitjpOsTi1ntGsqCl9-LVDQBXRaO2oicfIBsa_wGc01I1yXlib5jZf6zgSqottVa1-SIUSIM_8xKAFMjfWSJK3arE8VZgQl5zOt4EmeOaJSVYF1UfRo77y-DfZtu1ZFsa4TkpHtPIBfOUEE7a5WWiLYXODGjzo1NibDRc36FOFpUquEkeZIrag_o-XMlbWvUZvIdNFwYyg5d0U04DeRzThpktYS5DkA3jqICy2pmxsnmtGujQe2uPkthAZHux6uZRsuwprsgueqsC1ixRQ2ZhKdTLjRtyPh_3hGuGZzEoQxYpwQ2Kn6Rd88gAigo5hTJJ8U6o-BN7H2pgOECPUeLSKVaIicI4qvbneor44QPa9SH0k3XL2lJvr-BTWsO9vJ8ixRX1rk9Idd80QPKiFW1KDV0iMHhv57NiFFz039l6RtlSQAlGRMLS33Ye7CHHnjlJeLulyy6Sg290t4abmRinAlXNfbZbXIFzQCiKgil59gnl-lRI31szlozMlIfR_krZOqwtAtxKanfK4ixlE8ol7aBPTac-fiNbaIceC8m8l9r91YU-k-hd78QYDsYB4WIJpcas5OPTz4poUAifQVb6wXZAXb64zpb_AsJo4Y_u1Qngb7UzFpYrW0zfakNFlBMmkQXxLst4CV_QJLLGjRkmPWVSpMhzawMWhAQYd0XeviFSTDVCpCJibwoaUOm7JqnJoHfJD75qqz8M4_qDJfznvuWVVa4f0Jn_vMyOMi1lajGVejwAS9djSuhAnBtpGrpNihw5RlhaCpviDmC1g4JZpcSHkXMyGg-fcI9-m3WM-6aZiYkSHxgB2xhAuurdmVIpSRIUdM97O-ZQ1NyPgb4yia6YNUoMKnaPOuIAyWcafe3cH5H7Xv4Pu_QTnmsZANtqXVkl7ivsuc8UkMp6VQHGxWnGPODna2_uBLgAO3FSWoX6CHWCgMZyi6YWYHUfGlGFNNc9d45uu8OoE1aLeTTDrqHJubZf4AGjvMheQpkJ-h0B2mCUy9vvJoTAGMe9miZJRhihEohOVjd-Cnw9f5Y5laCDBTfGBvcX9EvinxHE72bZWbXCn9CB67xENrLJFaqZ4fbUGH-DcwZgxNj7bcJ6dWYAPUrc3kqDUh7c4fdOTd0oE5kzjiZ_z-AnSpdJIJ9uoQWhtgdUUeMwjDrOwU2mMSUCaARzI2PqiGikx0lirsXmXM0-iG5uo47uHO1vHo0F2L-d8yoyP2NANxrXrTwLHk2JvYKHKBWXSJw-blX9zomNAlCEZxMLDtBcbJehKuq5xmDBxjQaFh9mGhAlB_79SfD_WZ9K3vMbHJvu4wXs-7L53fGGO6hNi2ysdgYhnb4V7W7UZN97zxIYlBRLSWomVVZQyXqMAm4_7jqQUefeYZWAn5EDOlbbv8BvDv8xTO8GzbVJbsfstY-4iDYKpQXiydmquMDPU_-2KATgT0mW9hl-yP1OqKKmdyJCfCHHjkUd3MP1D7YiE7dcp06XSax7XrWR6XLPNEH_FFwq1pkB4q2NehTQG6f_DshcVA-9ytYZDsBNsrQKVnfOeqTlQ9pl9UTr0ftynvPDLFNin7moF-KhlT1Cwzi1R0zA8t5N8XK1BdZsSH8nmzJ8NOSf2Rbq3TI8daIYppZjUlJkeecWCZn4i9Un9oYfl4BPfmsFiF9-7Q11tl-QdeNIsCbWQYkmDQVaVPifi7-ymORcWyX60gFWON2CiGJ2K6rGpHWHmgntXD8pp75eW7N039rnKWRbvikZ5QY_sC3XmMxWyg0dykl1cugUGy_n5qRgWPsFFkIxrgA9zig2Em-6chB5Y471dYg3MRdygrfTqEeGf4msF35lWaHi32SZe2jIXiat9XaJpWaQGOcLS5rolNQD8TpKAa5ALb6ozpJ_NupYbVvybXHAt70DKgIfK0wTKl9FAKfekSHRurtoSW-YsP7GMfE-OcHuJAxzg3uG8Cz4O8VayvHKXDW6nK5m93KC_C1XjklRuDuFy17mm0tg0_5TGURfIq10",
                  "width": 88,
                  "height": 88,
                  "precision": 1
                }
              },
              "address": "Комсомольский просп., 28",
              "type": {
                "id": "5575d419cc1c724f5a8e1125",
                "rubricUrl": "/moscow/concert_hall",
                "code": "concert_hall",
                "type": "place",
                "status": "approved",
                "name": "Концертный зал",
                "namePlural": "концертные залы",
                "nameAcc": "в концертный зал",
                "nameGen": null,
                "nameAdj": null,
                "plural": null,
                "rubricPlacesUrl": "/moscow/concert_hall/places"
              },
              "tags": [
                {
                  "id": "5575d419cc1c724f5a8e1125",
                  "rubricUrl": "/moscow/concert_hall",
                  "code": "concert_hall",
                  "type": "place",
                  "status": "approved",
                  "name": "Концертный зал",
                  "namePlural": "концертные залы",
                  "nameAcc": "в концертный зал",
                  "nameGen": null,
                  "nameAdj": null,
                  "plural": null,
                  "rubricPlacesUrl": "/moscow/concert_hall/places"
                },
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
                  "code": "concert_hall"
                },
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
                  "name": "Фрунзенская",
                  "colors": [
                    "#cc0000"
                  ]
                },
                {
                  "name": "Спортивная",
                  "colors": [
                    "#cc0000"
                  ]
                },
                {
                  "name": "Парк культуры",
                  "colors": [
                    "#7f0000"
                  ]
                }
              ],
              "coordinates": {
                "longitude": 37.57964499999999,
                "latitude": 55.726876999999995
              },
              "bgColor": "#4b4b75",
              "logoColor": "#7c7cc2",
              "distance": null,
              "isFavorite": false
            },
            "headliners": {
              "title": null,
              "description": null
            },
            "session": {
              "date": "2118-11-13",
              "datetime": "2118-11-13T19:30:00",
              "ticket": {
                "id": "ODQ2fDk3MTM3fDEzMjg2MHwxNTQyMTI2NjAwMDAw",
                "price": {
                  "currency": "rub",
                  "min": 130000,
                  "max": 430000
                },
                "discountPercents": []
              },
              "hall": null
            }
          }
        ]
      }
    ]
  }
}
"""