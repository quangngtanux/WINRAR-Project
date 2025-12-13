from whistleblowing_commons.functions import trans

def get_understanding(parameters, lang):
    
    understanding = [
        dict(
            question=
                dict(
                    en="What happens if the Red Player steals ECU from the passive group?",
                    fr="Que se passe-t-il si le joueur Rouge vole des ECU au groupe passif ?",
                    vi="Chuyện gì sẽ xảy ra nếu Người chơi Đỏ đánh cắp ECU từ nhóm thụ động?"
                ),
            propositions=[
                dict(
                    en=f"The Red Player earns {parameters['STEALING_AMOUNT']} ECU, and the passive group "
                       f"loses {parameters['STEALING_LOSS']} ECU.",
                    fr=f"Le joueur Rouge gagne {parameters['STEALING_AMOUNT']} ECU, et le groupe passif "
                       f"perd {parameters['STEALING_LOSS']} ECU.",
                    vi=f"Người chơi Đỏ kiếm được {parameters['STEALING_AMOUNT']} ECU, và nhóm thụ động "
                       f"mất {parameters['STEALING_LOSS']} ECU."
                ),
                dict(
                    en=f"The Red Player earns {parameters['STEALING_LOSS']} ECU, and the passive group "
                       f"loses {parameters['STEALING_AMOUNT']} ECU.",
                    fr=f"Le joueur Rouge gagne {parameters['STEALING_LOSS']} ECU, et le groupe passif "
                       f"perd {parameters['STEALING_AMOUNT']} ECU.",
                    vi=f"Người chơi Đỏ kiếm được {parameters['STEALING_LOSS']} ECU, và nhóm thụ động "
                       f"mất {parameters['STEALING_AMOUNT']} ECU."
                ),
                dict(
                    en=f"The Red Player earns {parameters['STEALING_PENALTY']} ECU, and the passive group "
                       f"loses {parameters['REPORTING_COST']} ECU.",
                    fr=f"Le joueur Rouge gagne {parameters['STEALING_PENALTY']} ECU, et le groupe passif "
                       f"perd {parameters['REPORTING_COST']} ECU.",
                    vi=f"Người chơi Đỏ kiếm được {parameters['STEALING_PENALTY']} ECU, và nhóm thụ động "
                       f"mất {parameters['REPORTING_COST']} ECU."
                ),
            ],
            solution=0
        ),
        dict(
            question=dict(
                en="What happens if the Red Player has stolen ECU and the selected Blue Player reports the Red Player?",
                fr="Que se passe-t-il si le joueur Rouge a volé des ECU et que le joueur Bleu sélectionné signale le joueur Rouge ?",
                vi="Chuyện gì sẽ xảy ra nếu Người chơi Đỏ đã đánh cắp ECU và Người chơi Xanh được chọn báo cáo Người chơi Đỏ?"
            ),
            propositions=[
                dict(
                    en=f"If the Red player is penalized, they pay a penalty of {parameters['STEALING_PENALTY']} ECU. "
                       f"The Blue Player pays a reporting cost of {parameters['REPORTING_COST']} ECU.",
                    fr=f"Si le joueur Rouge est pénalisé, il paie une pénalité de {parameters['STEALING_PENALTY']} ECU. "
                       f"Le joueur Bleu paie un coût de signalement de {parameters['REPORTING_COST']} ECU.",
                    vi=f"Nếu Người chơi Đỏ bị phạt, họ sẽ phải trả một khoản phạt là {parameters['STEALING_PENALTY']} ECU. "
                       f"Người chơi Xanh phải trả một khoản chi phí báo cáo là {parameters['REPORTING_COST']} ECU."
                ),
                dict(
                    en=f"If the Red player is penalized, they pay a penalty of {parameters['STEALING_PENALTY']} ECU. "
                       f"The Blue Player pays a reporting cost of {parameters['REPORTING_COST']} ECU and receives "
                       f"a reward of {parameters['REPORTING_REWARD']} ECU.",
                    fr=f"Si le joueur Rouge est pénalisé, il paie une pénalité de {parameters['STEALING_PENALTY']} ECU. "
                       f"Le joueur Bleu paie un coût de signalement de {parameters['REPORTING_COST']} ECU et "
                       f"reçoit une récompense de {parameters['REPORTING_REWARD']} ECU.",
                    vi=f"Nếu Người chơi Đỏ bị phạt, họ sẽ phải trả một khoản phạt là {parameters['STEALING_PENALTY']} ECU. "
                       f"Người chơi Xanh phải trả một khoản chi phí báo cáo là {parameters['REPORTING_COST']} ECU và nhận được "
                       f"một phần thưởng là {parameters['REPORTING_REWARD']} ECU."
                ),
                dict(
                    en=f"If the Red player is not penalized, the Blue Player pays no reporting cost.",
                    fr=f"Si le joueur Rouge n'est pas pénalisé le joueur Bleu ne paie aucun coût de signalement.",
                    vi=f"Nếu Người chơi Đỏ không bị phạt, Người chơi Xanh sẽ không phải trả chi phí báo cáo nào."
                ),
            ],
            solution=1 if parameters['reward'] else 0,
        ),
        dict(
            question=dict(
                en="What happens if one Blue Player reports the Red player and the other Blue player does not?",
                fr="Que se passe-t-il si un joueur Bleu signale le joueur Rouge et que l'autre joueur Bleu ne le signale pas ?",
                vi="Chuyện gì sẽ xảy ra nếu một Người chơi Xanh báo cáo Người chơi Đỏ và Người chơi Xanh kia không báo cáo?"
            ),
            propositions=[
                dict(
                    en="Both decisions are implemented.",
                    fr="Les deux décisions sont mises en œuvre.",
                    vi="Cả hai quyết định đều được thực hiện."
                ),
                dict(
                    en="The Red Player is automatically penalized.",
                    fr="Le joueur Rouge est automatiquement pénalisé.",
                    vi="Người chơi Đỏ sẽ bị phạt tự động."
                ),
                dict(
                    en="The computer program randomly selects one Blue Player’s decision to implement.",
                    fr="Le programme informatique sélectionne au hasard la décision d'un joueur Bleu à mettre en œuvre.",
                    vi="Chương trình máy tính sẽ chọn ngẫu nhiên quyết định của một Người chơi Xanh để thực hiện."
                ),
            ],
            solution=2
        ),
    ]

    questionnaire = []
    for i, q in enumerate(understanding, start=1):
        question = dict(
            question_id = i,
            question=trans(q["question"], lang),
            propositions=[trans(p, lang) for p in q["propositions"]],
            solution=q["solution"]
        )
        questionnaire.append(question)
    return questionnaire
