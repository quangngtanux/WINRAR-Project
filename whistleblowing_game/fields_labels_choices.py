from whistleblowing_commons.config import Config
from whistleblowing_commons.functions import trans


def get_appropriate(lang="en"):
    return [
        (0, trans(dict(en="Very inappropriate", fr="Très inapproprié", vi="Rất không phù hợp"), lang)),
        (1, trans(dict(en="Inappropriate", fr="Inapproprié", vi="Không phù hợp"), lang)),
        (2, trans(dict(en="Rather inappropriate", fr="Plutôt inapproprié", vi="Khá không phù hợp"), lang)),
        (3, trans(dict(en="Rather appropriate", fr="Plutôt approprié", vi="Khá phù hợp"), lang)),
        (4, trans(dict(en="Appropriate", fr="Approprié", vi="Phù hợp"), lang)),
        (5, trans(dict(en="Very appropriate", fr="Très approprié", vi="Rất phù hợp"), lang)),
    ]


def taking_decision_choices(player):
    lang = player.session.vars["lang"]
    return [(False, trans(dict(en="No", fr="Non", vi="Không"), lang)),
            (True, trans(dict(en="Yes", fr="Oui", vi="Có"), lang))]


def reporting_decision_choices(player):
    lang = player.session.vars["lang"]
    return [(False, trans(dict(en="No", fr="Non", vi="Không"), lang)),
            (True, trans(dict(en="Yes", fr="Oui", vi="Có"), lang))]


def personal_opinion_choices(player):
    return get_appropriate(player.session.vars["lang"])


def society_opinion_choices(player):
    return get_appropriate(player.session.vars["lang"])


class Lexicon:
    taking_decision_label = dict(
        en="Do you want to steal ECU from the Passive group?",
        fr="Souhaitez-vous voler des ECU au groupe Passif ?",
        vi="Bạn có muốn lấy cắp ECU từ nhóm Bị động không?",
    )
    estimation_reporting_label = dict(
        en="Please indicate what you think is the likelihood that a Blue Player reports the Red Player:",
        fr="Veuillez indiquer quelles sont les chances qu'un joueur Bleu dénonce le joueur Rouge :",
        vi="Vui lòng cho biết khả năng một người chơi Xanh báo cáo người chơi Đỏ là bao nhiêu:",
    )
    reporting_decision_label = dict(
        en="Do you want to report the Red Player?",
        fr="Souhaitez-vous signaler le joueur Rouge ?",
        vi="Bạn có muốn báo cáo người chơi Đỏ không?",
    )
    taker_motivation_label = dict(
        en="Can you tell us what motivated your decision (as Red Player):",
        fr="Pouvez-vous nous expliquer ce qui a motivé votre décision (comme joueur Rouge) :",
        vi="Bạn có thể cho chúng tôi biết điều gì đã thúc đẩy quyết định của bạn (với tư cách là Người chơi Đỏ):"
    )
    reporter_motivation_label = dict(
        en="Can you tell us what motivated your decision (as Blue Player) to report or not the Red Player:",
        fr="Pouvez-vous nous expliquer ce qui a motivé votre décision (comme joueur Bleu) de signaler ou non le "
           "joueur Rouge :",
        vi="Bạn có thể cho chúng tôi biết điều gì đã thúc đẩy quyết định của bạn (với tư cách là Người chơi Xanh) "
           "báo cáo hoặc không báo cáo Người chơi Đỏ:"
    )
    personal_opinion_label = dict(
        en="Please evaluate according to your own opinion and independently of the opinion of others whether "
           "it is appropriate or not to report the Red Player. "
           "“Appropriate” behavior means the behavior that you personally consider to be “correct” or “moral”. "
           "The standard is, hence, your personal opinion, independently of the opinion of others. "
           "We kindly ask you to answer as precisely as possible with your own honest opinion. "
           "There is no right or wrong answer; you will not get any additional payment for your answer to this "
           "question.",
        fr="Veuillez évaluer, selon votre propre opinion et indépendamment de l'opinion des autres, s'il est "
           "approprié ou non de signaler le joueur Rouge. Un comportement 'approprié' signifie un comportement "
           "que vous considérez personnellement "
           "comme 'correct' ou 'moral'. La norme est donc votre opinion personnelle, indépendamment de celle "
           "des autres. Nous vous demandons de répondre aussi précisément que possible avec votre propre opinion "
           "honnête. Il n'y a pas de bonne ou de mauvaise réponse ; vous ne recevrez aucun paiement "
           "supplémentaire pour votre réponse à cette question.",
        vi="Vui lòng đánh giá theo ý kiến ​​của riêng bạn và độc lập với ý kiến ​​của người khác liệu việc báo cáo "
           "Người chơi Đỏ có phù hợp hay không. Hành vi 'Phù hợp' có nghĩa là hành vi mà bạn cá nhân coi là "
           "'đúng' hoặc 'đạo đức'. Tiêu chuẩn do đó là ý kiến ​​cá nhân của bạn, không phụ thuộc vào ý kiến ​​của "
           "người khác. Chúng tôi kính đề nghị bạn trả lời càng chính xác càng tốt với ý kiến ​​thành thật của "
           "bạn. Không có câu trả lời đúng hay sai; bạn sẽ không nhận được bất kỳ khoản thanh toán bổ sung nào "
           "cho câu trả lời của mình cho câu hỏi này.",
    )
    society_opinion_label = dict(
        en=f"Now, please evaluate the opinion of the society and independently of your opinion whether "
           f"it is appropriate or not to report the Red Player. 'Appropriate' behavior means the behavior "
           f"that you consider most people would agree upon as being 'correct' or 'moral'. "
           f"The standard is, hence, not your personal opinion, but your assessment of the opinion of the "
           f"society. We kindly ask you to answer as precisely as possible. For this question, you can "
           f"earn {Config.SOCIETY_OPTION_PAYOFF} ECU on top of your gains from the other parts of the experiment, "
           f"depending on your answer. The answers of the other participants will influence your payment for this "
           f"question. At the end, we will determine which answer to this question most of the other "
           f"participants gave. You will obtain {Config.SOCIETY_OPTION_PAYOFF} ECU if you gave the same answer as most of the "
           f"other participants. Example: suppose that you evaluate the action of reporting the Red Player "
           f"as 'Rather appropriate' and most of the other participants in this room evaluate the same "
           f"action as 'Rather appropriate'. Then, you earn {Config.SOCIETY_OPTION_PAYOFF} ECU for this question. "
           f"Note: all other participants have received the same instructions.",
        fr=f"Veuillez maintenant évaluer l'opinion de la société, indépendamment de votre propre opinion, sur le fait "
           f"qu'il soit approprié ou non de signaler le joueur Rouge. Un comportement 'approprié' signifie un comportement "
           f"que vous considérez comme étant généralement accepté par la majorité des gens comme 'correct' ou 'moral'. "
           f"La norme n'est donc pas votre opinion personnelle, mais votre évaluation de l'opinion de la société. "
           f"Nous vous demandons de répondre aussi précisément que possible. Pour cette question, vous pouvez "
           f"gagner {Config.SOCIETY_OPTION_PAYOFF} ECU en plus de vos gains des autres parties de l'expérience, "
           f"en fonction de votre réponse. Les réponses des autres participants influenceront votre paiement pour cette "
           f"question. À la fin, nous déterminerons quelle réponse à cette question a été donnée par la majorité des autres "
           f"participants. Vous obtiendrez {Config.SOCIETY_OPTION_PAYOFF} ECU si vous avez donné la même réponse que la majorité des "
           f"autres participants. Exemple : supposons que vous évaluez l'action de dénoncer le joueur Rouge "
           f"comme 'Plutôt approprié' et que la majorité des autres participants dans cette salle évaluent également cette "
           f"action comme 'Plutôt approprié'. Dans ce cas, vous gagnez {Config.SOCIETY_OPTION_PAYOFF} ECU pour cette question. "
           f"Note : tous les autres participants ont reçu les mêmes instructions.",
        vi=f"Vui lòng đánh giá ý kiến ​​của xã hội, độc lập với ý kiến ​​cá nhân của bạn về việc báo cáo Người chơi Đỏ "
           f"có phù hợp hay không. Hành vi 'Phù hợp' có nghĩa là hành vi mà bạn cho rằng hầu hết mọi người sẽ đồng ý là 'đúng' hoặc 'đạo đức'. "
           f"Tiêu chuẩn do đó không phải là ý kiến ​​cá nhân của bạn, mà là đánh giá của bạn về ý kiến ​​của xã hội. "
           f"Chúng tôi kính đề nghị bạn trả lời càng chính xác càng tốt. Đối với câu hỏi này, bạn có thể "
           f"kiếm được {Config.SOCIETY_OPTION_PAYOFF} ECU bên cạnh số tiền bạn kiếm được từ các phần khác của thí nghiệm, "
           f"tùy thuộc vào câu trả lời của bạn. Câu trả lời của những người tham gia khác sẽ ảnh hưởng đến khoản thanh toán của bạn cho câu hỏi này. "
           f"Cuối cùng, chúng tôi sẽ xác định câu trả lời nào cho câu hỏi này mà hầu hết những người tham gia khác đã đưa ra. "
           f"Bạn sẽ nhận được {Config.SOCIETY_OPTION_PAYOFF} ECU nếu bạn đưa ra cùng một câu trả lời như hầu hết những người tham gia khác. "
           f"Ví dụ: giả sử bạn đánh giá hành động báo cáo Người chơi Đỏ là 'Khá phù hợp' và hầu hết những người tham gia khác trong phòng này cũng đánh giá hành động đó là 'Khá phù hợp'. "
           f"Trong trường hợp đó, bạn kiếm được {Config.SOCIETY_OPTION_PAYOFF} ECU cho câu hỏi này.",
    )

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
