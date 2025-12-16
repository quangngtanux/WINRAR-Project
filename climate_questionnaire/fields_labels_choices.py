from whistleblowing_commons.functions import trans


# ======================================================================================================================
#
# Scale Choices
#
# ======================================================================================================================
def get_scale_action(lang):
    return [
        [-2, trans(dict(en="Not at all", fr="Pas du tout", vi="Hoàn toàn không"), lang)],
        [-1, trans(dict(en="-1", fr="-1", vi="-1"), lang)],
        [0, trans(dict(en="Moderately", fr="Modérément", vi="Vừa phải"), lang)],
        [1, trans(dict(en="1", fr="1", vi="1"), lang)],
        [2, trans(dict(en="A great deal", fr="Énormément", vi="Rất nhiều"), lang)]
    ]


def get_scale_policy(lang):
    return [
        [-2, trans(dict(en="Strongly oppose", fr="Fortement opposé(e)", vi="Hoàn toàn phản đối"), lang)],
        [-1, trans(dict(en="Somewhat oppose", fr="Plutôt opposé(e)", vi="Hơi phản đối"), lang)],
        [0, trans(dict(en="Neither support nor oppose", fr="Ni favorable ni opposé(e)",
                       vi="Không phản đối cũng không ủng hộ"), lang)],
        [1, trans(dict(en="Somewhat support", fr="Plutôt favorable", vi="Hơi ủng hộ"), lang)],
        [2, trans(dict(en="Strongly support", fr="Fortement favorable", vi="Hoàn toàn ủng hộ"), lang)]
    ]


def get_scale_certainty(lang):
    return [
        [-2, trans(dict(en="Very uncertain", fr="Très incertain", vi="Rất không chắc chắn"), lang)],
        [-1, trans(dict(en="Uncertain", fr="Incertain", vi="Không chắc chắn"), lang)],
        [1, trans(dict(en="Certain", fr="Certain", vi="Chắc chắn"), lang)],
        [2, trans(dict(en="Very certain", fr="Très certain", vi="Rất chắc chắn"), lang)],
    ]


def get_scale_frequency_info(lang):
    return [
        [5, trans(dict(en="Daily", fr="Quotidiennement", vi="Hàng ngày"), lang)],
        [4, trans(dict(en="Twice per week", fr="Deux fois par semaine", vi="Hai lần mỗi tuần"), lang)],
        [3, trans(dict(en="Once per week", fr="Une fois par semaine", vi="Một lần mỗi tuần"), lang)],
        [2, trans(dict(en="Twice per month", fr="Deux fois par mois", vi="Hai lần mỗi tháng"), lang)],
        [1, trans(dict(en="Once per month", fr="Une fois par mois", vi="Một lần mỗi tháng"), lang)],
        [0, trans(dict(en="Never", fr="Jamais", vi="Không bao giờ"), lang)]
    ]


def get_scale_expectations(lang):
    return [
        [-2, trans(dict(en="Very unlikely", fr="Très improbable", vi="Rất khó xảy ra"), lang)],
        [-1, trans(dict(en="Somewhat unlikely", fr="Plutôt improbable", vi="Hơi khó xảy ra"), lang)],
        [1, trans(dict(en="Somewhat likely", fr="Plutôt probable", vi="Hơi có khả năng xảy ra"), lang)],
        [2, trans(dict(en="Very likely", fr="Très probable", vi="Rất có khả năng xảy ra"), lang)]
    ]


def get_scale_agreement(lang):
    return [
        [-2, trans(dict(en="Strongly disagree", fr="Fortement en désaccord", vi="Hoàn toàn không đồng ý"), lang)],
        [-1, trans(dict(en="Somewhat disagree", fr="Plutôt en désaccord", vi="Hơi không đồng ý"), lang)],
        [0, trans(dict(en="Neither agree nor disagree", fr="Ni d'accord ni en désaccord",
                       vi="Không đồng ý cũng không phản đối"), lang)],
        [1, trans(dict(en="Somewhat agree", fr="Plutôt d'accord", vi="Hơi đồng ý"), lang)],
        [2, trans(dict(en="Strongly agree", fr="Fortement d'accord", vi="Hoàn toàn đồng ý"), lang)]
    ]


def get_scale_income(lang):
    return [
        [0, trans(dict(en="From 0$ to 1250$", fr="De 0€ à 1250€", vi="Từ 0$ đến 5.000.000 VND"), lang)],
        [1, trans(dict(en="From 1250$ to 2000$", fr="De 1250€ à 2000€", vi="Từ 5.000.000 đến 10.000.000 VND"), lang)],
        [2, trans(dict(en="From 2000$ to 4000$", fr="De 2000€ à 4000€", vi="Từ 10.000.000 đến 15.000.000 VND"), lang)],
        [3, trans(dict(en="From 4000$ to 6000$", fr="De 4000€ à 6000€", vi="Từ 15.000.000 đến 30.000.000 VND"), lang)],
        [4, trans(dict(en="From 6000$ to 8000$", fr="De 6000€ à 8000€", vi="Từ 30.000.000 đến 45.000.000 VND"), lang)],
        [5, trans(dict(en="From 8000$ to 12,500$", fr="De 8000€ à 12 500€", vi="Từ 45.000.000 đến 60.000.000 VND"), lang)],
        [6, trans(dict(en="More than 12,500$", fr="Plus de 12 500€", vi="Hơn 60.000.000"), lang)],
        [999, trans(dict(en="I prefer not to say", fr="Je préfère ne pas répondre", vi="Tôi không muốn trả lời"), lang)]
    ]


def get_scale_education(lang):
    return [
        [0, trans(dict(
            en="Primary or lower secondary education",
            fr="Primaire ou collège",
            vi="Giáo dục tiểu học hoặc trung học cơ sở"
        ), lang)],
        [1, trans(dict(
            en="Upper secondary education",
            fr="Lycée (Baccalauréat)",
            vi="Giáo dục trung học phổ thông"
        ), lang)],
        [2, trans(dict(
            en="Non-university post-secondary education",
            fr="Formation post-secondaire non universitaire",
            vi="Giáo dục sau trung học không thuộc đại học"
        ), lang)],
        [3, trans(dict(
            en="Undergraduate education (bachelor)",
            fr="Licence (Bachelor)",
            vi="Giáo dục đại học (cử nhân)"
        ), lang)],
        [4, trans(dict(
            en="Postgraduate education (Master or PhD)",
            fr="Master ou Doctorat",
            vi="Giáo dục sau đại học (Thạc sĩ hoặc Tiến sĩ)"
        ), lang)],
        [999, trans(dict(
            en="I prefer not to say",
            fr="Je préfère ne pas répondre",
            vi="Tôi không muốn trả lời"
        ), lang)]
    ]


def get_options_bdm(lang):
    return [
        ['A', trans(dict(en='Option A', fr='Option A', vi='Lựa chọn A'), lang)],
        ['B', trans(dict(en='Option B', fr='Option B', vi='Lựa chọn B'), lang)]
    ]


# ======================================================================================================================
#
# DYNAMIC CHOICES METHODS
#
# ======================================================================================================================
def climate_exists_choices(player):
    lang = player.session.vars['lang']
    return [
        [True, trans(dict(en="Yes", fr="Oui", vi="Có"), lang)],
        [False, trans(dict(en="No", fr="Non", vi="Không"), lang)]
    ]


def policy_fight_choices(player):
    lang = player.session.vars['lang']
    return [
        [1, trans(dict(en="Yes", fr="Oui", vi="Có"), lang)],
        [0, trans(dict(en="No", fr="Non", vi="Không"), lang)],
        [-1, trans(dict(
            en="I don't know/I do not want to answer",
            fr="Je ne sais pas/Je ne souhaite pas répondre",
            vi="Tôi không biết/Tôi không muốn trả lời"
        ), lang)
         ]
    ]


def expectations_policy_household_choices(player):
    lang = player.session.vars['lang']
    return [
        [-2, trans(dict(en="Lose a lot", fr="Perdre beaucoup", vi="Mất rất nhiều"), lang)],
        [-1, trans(dict(en="Lose", fr="Perdre", vi="Mất"), lang)],
        [0, trans(dict(en="Neither win or lose", fr="Ni gagner ni perdre", vi="Không lãi cũng không lỗ"), lang)],
        [1, trans(dict(en="Win", fr="Gagner", vi="Được lợi"), lang)],
        [2, trans(dict(en="Win a lot", fr="Gagner beaucoup", vi="Được lợi rất nhiều"), lang)],
    ]


def agreement_policy_choices(player):
    lang = player.session.vars['lang']
    return get_scale_policy(lang)


def climate_knowledge_choices(player):
    lang = player.session.vars['lang']
    return [
        [0, trans(dict(en="Not at all", fr="Pas du tout", vi="Không hề"), lang)],
        [1, trans(dict(en="A little", fr="Un peu", vi="Một chút"), lang)],
        [2, trans(dict(en="Moderately", fr="Modérément", vi="Ở mức vừa phải"), lang)],
        [3, trans(dict(en="A lot", fr="Beaucoup", vi="Nhiều"), lang)],
        [4, trans(dict(en="A great deal", fr="Énormément", vi="Rất nhiều"), lang)]
    ]


def info_freq_choices(player):
    return get_scale_frequency_info(player.session.vars['lang'])


def climate_info_freq_choices(player):
    return get_scale_frequency_info(player.session.vars['lang'])


def climate_threat_choices(player):
    lang = player.session.vars['lang']
    return [
        [3, trans(dict(
            en="Very serious threat",
            fr="Une menace très sérieuse",
            vi="Mối đe dọa rất nghiêm trọng"
        ), lang)],
        [2, trans(dict(
            en="Somewhat serious threat",
            fr="Une menace assez sérieuse",
            vi="Mối đe dọa tương đối nghiêm trọng"
        ), lang)],
        [1, trans(dict(
            en="Not a threat at all",
            fr="Pas une menace du tout",
            vi="Hoàn toàn không phải là mối đe dọa"
        ), lang)],
        [0, trans(dict(
            en="Don’t know",
            fr="Ne sais pas",
            vi="Không biết"
        ), lang)]
    ]


def limit_flying_choices(player): return get_scale_action(player.session.vars['lang'])


def limit_driving_choices(player): return get_scale_action(player.session.vars['lang'])


def electric_vehicle_choices(player): return get_scale_action(player.session.vars['lang'])


def limit_beef_choices(player): return get_scale_action(player.session.vars['lang'])


def limit_heating_choices(player): return get_scale_action(player.session.vars['lang'])


def tax_flying_choices(player): return get_scale_policy(player.session.vars['lang'])


def tax_fossil_choices(player): return get_scale_policy(player.session.vars['lang'])


def ban_polluting_choices(player): return get_scale_policy(player.session.vars['lang'])


def subsidy_lowcarbon_choices(player): return get_scale_policy(player.session.vars['lang'])


def climate_fund_choices(player): return get_scale_policy(player.session.vars['lang'])


def expectations_droughts_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_eruptions_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_sea_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_agriculture_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_living_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_migration_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_conflicts_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_extinction_choices(player): return get_scale_expectations(player.session.vars['lang'])


def expectations_policy_economy_choices(player): return get_scale_agreement(player.session.vars['lang'])


def expectations_policy_cc_choices(player): return get_scale_agreement(player.session.vars['lang'])


def income_choices(player): return get_scale_income(player.session.vars['lang'])


def education_choices(player): return get_scale_education(player.session.vars['lang'])


def choice_1_choices(player): return get_options_bdm(player.session.vars['lang'])


def choice_2_choices(player): return get_options_bdm(player.session.vars['lang'])


def choice_3_choices(player): return get_options_bdm(player.session.vars['lang'])


def choice_4_choices(player): return get_options_bdm(player.session.vars['lang'])


def choice_5_choices(player): return get_options_bdm(player.session.vars['lang'])


def choice_6_choices(player): return get_options_bdm(player.session.vars['lang'])


def choice_7_choices(player): return get_options_bdm(player.session.vars['lang'])


# ======================================================================================================================
#
# FIELDS LABELS
#
# ======================================================================================================================
class Lexicon:
    climate_exists_label = dict(
        en="Do you think climate change is a real phenomenon?",
        fr="Pensez-vous que le changement climatique soit un phénomène réel ?",
        vi="Bạn có nghĩ rằng biến đổi khí hậu là một hiện tượng có thật không?"
    )
    narrative_elicitation_label = dict(
        en=(
            "In your opinion, what explains the facts described in the text before (such as the reported rise in "
            "global temperatures and more extreme weather events)? <br><br>"
            "Please describe the <b>causes</b> of the facts attributed to climate change, and <b>explain</b> "
            "how these causes contribute to these facts and might be connected to each other.  <br><br> "
            "Explain your reasoning in full sentences. "
            "There is no good or wrong answer, respond according to your sincere and personal opinion. <br> "
            "[min. 50 words]"),
        fr=("Selon vous, quelles sont les causes des faits décrits dans le texte précédent (comme la hausse des "
            "températures mondiales et l'augmentation des événements météorologiques extrêmes) ? <br><br>"
            "Veuillez décrire les <b>causes</b> des faits attribués au changement climatique, et "
            "<b>expliquer</b> comment ces causes contribuent à ces faits et pourraient être liées entre elles. <br><br> "
            "Expliquez votre raisonnement avec des phrases complètes. "
            "Il n'y a pas de bonne ou de mauvaise réponse, répondez selon votre opinion sincère et personnelle. <br> "
            "[min. 50 mots]"),
        vi=(
            "Theo bạn, nguyên nhân của các hiện tượng được miêu tả trong đoạn văn trước đó là gì? (chẳng hạn như các số liệu về mức tăng nhiệt độ trung bình toàn cầu và các hiện tượng thời tiết cực đoan)? <br><br>"
            "Vui lòng mô tả các <b>nguyên nhân</b> của những hiện tượng biến đổi khí hậu, và <b>giải thích</b> tại sao những nguyên nhân này góp phần tạo ra các hiện tượng đó, cũng như các nguyên nhân này có thể liên hệ với nhau như thế nào. <br><br> "
            "Hãy giải thích lập luận của bạn bằng các câu hoàn chỉnh. Không có câu trả lời đúng hay sai; hãy trả lời theo ý kiến cá nhân theo những gì bạn nghĩ của bạn. <br> [tối thiểu 50 từ]")
    )
    narrative_confidence_label = dict(
        en="On a scale from 0 (very unconfident) to 100 (very confident), how confident are you about the explanation "
           "you provided in the previous question?",
        fr="Sur une échelle de 0 (très peu confiant) à 100 (très confiant), à quel point êtes-vous confiant "
           "concernant l'explication que vous avez fournie dans la question précédente ?",
        vi="Trên thang điểm từ 0 (rất không tự tin) đến 100 (rất tự tin), bạn tự tin đến mức nào về lời giải thích "
           "mà bạn đã đưa ra ở câu hỏi trước?"
    )
    confidence_policy_label = dict(
        en="On a scale from 0 (very unconfident) to 100 (very confident), how confident are you about the answer you "
           "provided in the previous question on what measures and solutions your government should consider to fight "
           "climate change?",
        fr="Sur une échelle de 0 (très peu confiant) à 100 (très confiant), à quel point êtes-vous confiant "
           "concernant la réponse que vous avez fournie dans la question précédente sur les mesures et solutions que "
           "votre gouvernement devrait envisager pour lutter contre le changement climatique ?",
        vi="Trên thang điểm từ 0 (rất không tự tin) đến 100 (rất tự tin), bạn tự tin đến mức nào về câu trả lời bạn đã đưa ra ở câu hỏi trước liên quan đến các biện pháp và giải pháp mà chính phủ nên xem xét để chống biến đổi khí hậu?"
    )
    policy_fight_label = dict(
        en="In your opinion, do you think your country should fight climate change?",
        fr="Selon vous, votre pays devrait-il lutter contre le changement climatique ?",
        vi="Theo bạn, đất nước bạn có nên đấu tranh chống biến đổi khí hậu không?"
    )
    policy_narrative_label = dict(
        en="Why?", fr="Pourquoi XXX ?", vi="Tại sao?"
    )
    expectations_policy_economy_label = dict(
        en="The solution I mentioned would have a positive effect on my country’s economy and employment",
        fr="La solution que j'ai mentionnée aurait un effet positif sur l'économie et l'emploi de mon pays",
        vi="Giải pháp mà tôi đã nêu sẽ có tác động tích cực đến kinh tế và tình hình việc làm ở nước tôi."
    )
    expectations_policy_cc_label = dict(
        en="The solution I mentioned would help limit and/or mitigate the consequences of climate change",
        fr="La solution que j'ai mentionnée aiderait à limiter et/ou atténuer les conséquences du changement climatique",
        vi="Giải pháp mà tôi đã nêu sẽ giúp hạn chế và/hoặc giảm nhẹ các hậu quả của biến đổi khí hậu."
    )
    expectations_policy_household_label = dict(
        en="My household will win or lose financially from the solution I mentioned",
        fr="Mon foyer gagnera ou perdra financièrement de la solution que j'ai mentionnée",
        vi="Gia đình của tôi sẽ được lợi hoặc chịu thiệt về tài chính từ giải pháp mà tôi đã nêu."
    )
    agreement_policy_label = dict(
        en="Do you support or oppose the solution you provided?",
        fr="Êtes-vous favorable ou opposé(e) à la solution que vous avez fournie ?",
        vi="Bạn ủng hộ hay phản đối giải pháp mà bạn đã đề xuất?"
    )
    climate_knowledge_label = dict(
        en="How knowledgeable do you consider yourself about climate change?",
        fr="À quel point vous considérez-vous informé(e) sur le changement climatique ?",
        vi="Bạn đánh giá kiến thức về biến đổi khí hậu của mình như thế nào?"
    )
    rank_coal_label = dict(
        en="Rank of Coal-fired power station",
        fr="Classement centrale charbon",
        vi="Xếp hạng của nhà máy điện than"
    )
    rank_gas_label = dict(
        en="Rank of Gas-fired power plant",
        fr="Classement centrale gaz",
        vi="Xếp hạng của nhà máy điện khí"
    )
    rank_nuclear_label = dict(
        en="Rank of Nuclear power plant",
        fr="Classement centrale nucléaire",
        vi="Xếp hạng của nhà máy điện hạt nhân"
    )
    info_freq_label = dict(
        en="Over the past 3 months, how often did you acquire information and/or news? For information and news we refer to national, international, and regional/local news, as well as other news facts.",
        fr="Au cours des 3 derniers mois XXX",
        vi="Trong 3 tháng vừa qua, bạn đã tiếp nhận thông tin và/hoặc tin tức với tần suất như thế nào? Ở đây, “thông tin và tin tức” bao gồm tin tức quốc gia, quốc tế, khu vực/địa phương, cũng như các tin tức, sự kiện khác."
    )
    use_tv_label = dict(en="Television (e.g., national news, cable news)", fr="Télévision", vi="Truyền hình (ví dụ như tin thời sự quốc gia, tin trên đài truyền hình cáp)")
    use_newspapers_label = dict(en="Printed Newspapers", fr="Journaux", vi="Báo in")
    use_radio_label = dict(en="Radio or podcasts", fr="Radio", vi="Radio hoặc podcasts")
    use_social_label = dict(en="Social media platforms", fr="Réseaux sociaux", vi="Mạng xã hội")
    use_online_label = dict(en="News media websites or apps", fr="Sites web en ligne", vi="Tin tức trên các trang web truyền thông hoặc các ứng dụng điện thoại")
    use_newsletters_label = dict(en="Newsletters or email subscriptions", fr="Bulletins d'information", vi="Bảng tin được gởi qua thư hoặc qua tài khoản mail được đăng ký")
    climate_info_freq_label = dict(
        en="Over the past 3 months, how often did you acquire information and/or news about <b>climate change</b>? For information and news we refer to national, international, and regional/local news, as well as other news facts.",
        fr=" XXX sur le changement climatique ?",
        vi="Trong 3 tháng vừa qua, bạn đã tiếp nhận thông tin và/hoặc tin tức <b>về biến đổi khí hậu</b> với tần suất như thế nào? Ở đây, “thông tin và tin tức” bao gồm tin tức quốc gia, quốc tế, khu vực/địa phương, cũng như các tin tức, sự kiện khác."
    )
    use_tv_climate_label = dict(en="Television (e.g., national news, cable news)", fr="Télévision", vi="Truyền hình (ví dụ như tin thời sự quốc gia, tin trên đài truyền hình cáp)")
    use_newspapers_climate_label = dict(en="Printed Newspapers", fr="Journaux", vi="Báo in")
    use_radio_climate_label = dict(en="Radio or podcasts", fr="Radio", vi="Radio hoặc podcasts")
    use_social_climate_label = dict(en="Social media platforms", fr="Réseaux sociaux", vi="Mạng xã hội")
    use_online_climate_label = dict(en="News media websites or apps", fr="Sites web en ligne", vi="Tin tức trên các trang web truyền thông hoặc các ứng dụng điện thoại")
    use_newsletters_climate_label = dict(en="Newsletters or email subscriptions", fr="Bulletins d'information", vi="Bảng tin được gởi qua thư hoặc qua tài khoản mail được đăng ký")
    climate_threat_label = dict(
        en="Do you think climate change will be a threat to people in your country in the next 20 years?",
        fr="Pensez-vous que le changement climatique sera une menace XXX",
        vi="Bạn có nghĩ rằng biến đổi khí hậu sẽ là một mối đe dọa đối với người dân ở Việt Nam trong 20 năm tới không?"
    )
    expectations_droughts_label = dict(en="Severe droughts and heatwaves", fr="Sécheresses sévères", vi="Hạn hán nghiêm trọng và các đợt nắng nóng kéo dài")
    expectations_eruptions_label = dict(en="More frequent volcanic eruptions", fr="Éruptions volcaniques", vi="Có nhiều vụ phun trào núi lửa hơn ")
    expectations_sea_label = dict(en="Rising sea levels", fr="Montée du niveau de la mer", vi="Mực nước biển dâng cao")
    expectations_agriculture_label = dict(
        en="Lower agricultural production", fr="Perturbation agricole", vi="Sản lượng nông nghiệp thấp hơn")
    expectations_living_label = dict(en="Drop in standards of living", fr="Conditions de vie", vi="Chất lượng sống giảm")
    expectations_migration_label = dict(en="Larger migration flows", fr="Migrations humaines", vi="Dòng người di cư nhiều hơn")
    expectations_conflicts_label = dict(en="More armed conflicts", fr="Conflits", vi="Các cuộc xung đột vũ trang xuất hiện nhiều hơn")
    expectations_extinction_label = dict(en="Extinction of humankind", fr="Extinction des espèces", vi="Loài người sẽ bị tuyệt chủng")
    limit_flying_label = dict(en="Limit flying", fr="Limiter les vols", vi="Hạn chế đi máy bay")
    limit_driving_label = dict(en="Limit driving", fr="Limiter la conduite", vi="Hạn chế lái xe")
    electric_vehicle_label = dict(en="Have an electric vehicle", fr="Véhicule électrique", vi="Xe điện")
    limit_beef_label = dict(en="Limit beef consumption", fr="Limiter le boeuf", vi="Hạn chế thịt bò")
    limit_heating_label = dict(en="Limit heating or cooling your home", fr="Limiter le chauffage", vi="Hạn chế sưởi ấm")
    income_label = dict(en="Thinking about your household, what would you estimate is its total net monthly "
                            "income on average (after taxes and deductions)? Please include salaries, pensions, family allowances, "
                            "unemployment benefits, or any other regular income.",
                        fr="Question revenu...",
                        vi="Câu hỏi về thu nhập...")
    education_label = dict(en="What is the highest education level that you have achieved?",
                           fr="Question éducation...",
                           vi="Câu hỏi về giáo dục...")

    @staticmethod
    def _get_field_label(field_name, lang):
        content = getattr(Lexicon, f"{field_name}_label", None)
        if content:
            return content.get(lang, content.get('en', 'MISSING TRANSLATION'))
        return f"Label for '{field_name}' not found"

    @staticmethod
    def get_fields_labels(field_names: list, lang: str):
        fields_labels = dict()
        for field in field_names:
            fields_labels[field] = Lexicon._get_field_label(field, lang)
        return fields_labels
