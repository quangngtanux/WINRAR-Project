from whistleblowing_commons.functions import trans
from otree.api import cu


def relevant_likert(lang="en"):
    return [
        (0, trans(dict(
            en="not at all relevant (this consideration has nothing to do with my judgments of right or wrong)",
            fr="pas du tout pertinent (cette considération n'a rien à voir avec mes jugements de bien ou de mal)",
            vi="không liên quan gì cả (cân nhắc này không liên quan gì đến đánh giá đúng hay sai của tôi)"
        ), lang)),
        (1, trans(dict(en="not very relevant", fr="pas très pertinent", vi="không quá liên quan"), lang)),
        (2, trans(dict(en="slightly relevant", fr="légèrement pertinent", vi="hơi liên quan"), lang)),
        (3, trans(dict(en="somewhat relevant", fr="assez pertinent", vi="khá liên quan"), lang)),
        (4, trans(dict(en="very relevant", fr="très pertinent", vi="rất liên quan"), lang)),
        (5, trans(dict(en="extremely relevant", fr="extrêmement pertinent", vi="cực kỳ liên quan"), lang)),
    ]


def agreement_likert(lang="en"):
    return [
        (0, trans(dict(en="Strongly disagree", fr="Fortement en désaccord", vi="Hoàn toàn không đồng ý"), lang)),
        (1,
         trans(dict(en="Moderately disagree", fr="Modérément en désaccord", vi="Không đồng ý mức độ vừa phải"), lang)),
        (2, trans(dict(en="Slightly disagree", fr="Légèrement en désaccord", vi="Không đồng ý một chút"), lang)),
        (3, trans(dict(en="Slightly agree", fr="Légèrement d'accord", vi="Đồng ý một chút"), lang)),
        (4, trans(dict(en="Moderately agree", fr="Modérément d'accord", vi="Đồng ý mức độ vừa phải"), lang)),
        (5, trans(dict(en="Strongly agree", fr="Fortement d'accord", vi="Hoàn toàn đồng ý"), lang)),
    ]


def fairness_1_choices(player):
    return relevant_likert(player.session.vars["lang"])


def fairness_2_choices(player):
    return relevant_likert(player.session.vars["lang"])


def fairness_3_choices(player):
    return agreement_likert(player.session.vars["lang"])


def loyalty_1_choices(player):
    return relevant_likert(player.session.vars["lang"])


def loyalty_2_choices(player):
    return relevant_likert(player.session.vars["lang"])


def loyalty_3_choices(player):
    return agreement_likert(player.session.vars["lang"])


def morally_good_person_choices(player):
    lang = player.session.vars["lang"]
    return [
        (1, trans(dict(
            en="Someone who is fair and just, impartial and unprejudiced",
            fr="Quelqu'un qui est juste et équitable, impartial et sans préjugés",
            vi="Ai đó công bằng và chính trực, không thiên vị và không định kiến"
        ), lang)),
        (0, trans(dict(
            en="Someone who is loyal and faithful, devoted and dependable",
            fr="Quelqu'un qui est loyal et fidèle, dévoué et fiable",
            vi="Ai đó trung thành và đáng tin cậy"
        ), lang)),
    ]


def friend_choice_choices(player):
    lang = player.session.vars["lang"]
    return [
        (1, trans(dict(
            en="Someone who is fair and just to others, who is impartial and unprejudiced regardless of "
               "how it affects their family and friends",
            fr="Quelqu'un qui est juste et équitable envers les autres, impartial et sans préjugés, même "
               "si cela affecte sa famille et ses amis",
            vi="Ai đó công bằng và chính trực với người khác, không thiên vị và không định kiến bất kể "
               "nó ảnh hưởng như thế nào đến gia đình và bạn bè của họ"
        ), lang)),
        (0, trans(dict(
            en="Someone who is loyal and faithful to their family and friends, who is devoted and "
               "dependable regardless of how it affects outsiders",
            fr="Quelqu'un qui est loyal et fidèle à sa famille et à ses amis, dévoué et fiable même si "
               "cela affecte des personnes extérieures",
            vi="Ai đó trung thành và đáng tin cậy với gia đình và bạn bè của họ, tận tâm và đáng tin cậy "
               "bất kể nó ảnh hưởng như thế nào đến người ngoài"
        ), lang))]


def gender_choices(player):
    lang = player.session.vars["lang"]
    return [
        ("F", trans(dict(en="Female", fr="Femme", vi="Nữ"), lang)),
        ("M", trans(dict(en="Male", fr="Male", vi="Nam"), lang)),
        ("NB", trans(dict(en="Non-binary", fr="Non binaire", vi="Không nhị phân"), lang)),
        ("NSP", trans(dict(en="Prefer no to say", fr="Ne souhaite pas répondre", vi="Không muốn nói"), lang)),
    ]


def highest_diploma_choices(player):
    lang = player.session.vars["lang"]
    return [
        (0,
         trans(dict(en="No formal education", fr="Aucune éducation formelle", vi="Không có giáo dục chính quy"), lang)),
        (1, trans(dict(en="Primary education", fr="Enseignement primaire", vi="Giáo dục tiểu học"), lang)),
        (2, trans(dict(en="Secondary education", fr="Enseignement secondaire", vi="Giáo dục trung học"), lang)),
        (3, trans(dict(en="Bachelor’s degree", fr="Licence", vi="Cử nhân"), lang)),
        (4, trans(dict(en="Master’s degree", fr="Master", vi="Thạc sĩ"), lang)),
        (5, trans(dict(en="Doctorate or higher", fr="Doctorat ou supérieur", vi="Tiến sĩ hoặc cao hơn"), lang)),
    ]

class Lexicon:
    fairness_1_label = dict(
        en="... whether or not someone acted unfairly",
        fr="... si oui ou non quelqu'un a agi de manière injuste",
        vi="... liệu ai đó có hành xử không công bằng hay không"
    )
    fairness_2_label = dict(
        en="... whether or not someone was denied his or her rights",
        fr="... si oui ou non quelqu'un a renié à ses droits",
        vi="... liệu ai đó có bị từ chối quyền lợi của mình hay không"
    )
    fairness_3_label = dict(
        en="Justice is the most important requirement for a society",
        fr="La justice est primordiale pour une société",
        vi="Công lý là yêu cầu quan trọng nhất đối với một xã hội"
    )
    loyalty_1_label = dict(
        en="... whether or not someone did something to betray his or her group",
        fr="... si oui ou non quelqu'un a fait quelque chose pour trahir son groupe",
        vi="... liệu ai đó có làm điều gì đó để phản bội nhóm của mình hay không"
    )
    loyalty_2_label = dict(
        en="... whether or not someone showed a lack of loyalty",
        fr="... si oui ou non quelqu'un a fait preuve d'un manque de loyauté",
        vi="... liệu ai đó có thể hiện sự thiếu trung thành hay không"
    )
    loyalty_3_label = dict(
        en="People should be loyal to their family members, even when they have done something wrong",
        fr="Les gens doivent être loyaux avec les membres de leur famille, même lorsqu'ils ont fait quelque "
           "chose de mal",
        vi="Mọi người nên trung thành với các thành viên trong gia đình, ngay cả khi họ đã làm điều gì đó sai trái"
    )
    morally_good_person_label = dict(
        en="Objectively speaking, who do you think is the more morally good person?",
        fr="Objectivement parlant, qui est la personne la plus morale selon toi ?",
        vi="Nói một cách khách quan, bạn nghĩ ai là người có đạo đức hơn?"
    )
    friend_choice_label = dict(
        en="Who would you rather be friends with?",
        fr="Avec qui préféreriez-vous être ami(e) ?",
        vi="Bạn muốn làm bạn với ai hơn?"
    )
    share_friend_stranger_label = dict(
        en=f"How much of your {cu(1000)} would you give to your friend, if the rest goes to a "
           "random stranger from your country?",
        fr=f"Sur vos {cu(1000)}, combien donneriez-vous à votre ami(e), si le reste allait à un(e) "
           f"inconnu(e) pris(e) au hasard dans votre pays ?",
        vi=f"Bạn sẽ cho bạn của mình bao nhiêu trong số {cu(1000)} của bạn, nếu phần còn lại sẽ "
           "đi đến một người lạ ngẫu nhiên từ đất nước của bạn?"
    )
    gender_label = dict(
        en="What is your gender?",
        fr="Quel est votre genre ?",
        vi="Giới tính của bạn là gì?"
    )
    age_label = dict(
        en="What is your age?",
        fr="Quel est votre âge ?",
        vi="Tuổi của bạn là bao nhiêu?"
    )
    highest_diploma_label = dict(
        en="What is the highest level of education you have completed?",
        fr="Quel est le niveau d'études le plus élevé que vous ayez terminé ?",
        vi="Trình độ học vấn cao nhất bạn đã hoàn thành là gì?"
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
