form = QuestionForm()
if form.validate_on_submit():
    add_question = Questions()
    add_question.user_id = form.user_id.data
    add_question.question = form.question.data
    db_session.add(add_question)
    db_session.commit()