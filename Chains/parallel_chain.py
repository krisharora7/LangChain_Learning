from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()
text = '''
Ensemble learning is a method where multiple models are combined instead of using just one. Even if individual models are weak, combining their results gives more accurate and reliable predictions.

Uses multiple models together to improve overall accuracy.
Reduces errors by balancing mistakes across models.
Works on a simple idea similar to combining opinions from a group.

Types of Ensemble Learning
There are three main types of ensemble methods:

Bagging (Bootstrap Aggregating): Models are trained independently on different random subsets of the training data. Their results are then combined—usually by averaging (for regression) or voting (for classification). This helps reduce variance and prevents overfitting.
Boosting: Models are trained one after another. Each new model focuses on fixing the errors made by the previous ones. The final prediction is a weighted combination of all models, which helps reduce bias and improve accuracy.
Stacking (Stacked Generalization): Multiple different models (often of different types) are trained and their predictions are used as inputs to a final model, called a meta-model. The meta-model learns how to best combine the predictions of the base models, aiming for better performance than any individual model.
Technique

Category

Description

Random Forest

Bagging

Random forest constructs multiple decision trees on bootstrapped subsets of the data and aggregates their predictions for final output, reducing overfitting and variance.

Random Subspace Method

Bagging

Trains models on random subsets of input features to enhance diversity and improve generalization while reducing overfitting.

Gradient Boosting Machines (GBM)

Boosting

Gradient Boosting Machines sequentially builds decision trees, with each tree correcting errors of the previous ones, enhancing predictive accuracy iteratively.

Extreme Gradient Boosting (XGBoost)

Boosting

XGBoost do optimizations like tree pruning, regularization and parallel processing for robust and efficient predictive models.

AdaBoost (Adaptive Boosting)

Boosting

AdaBoost focuses on challenging examples by assigning weights to data points. Combines weak classifiers with weighted voting for final predictions.

CatBoost

Boosting

CatBoost specialize in handling categorical features natively without extensive preprocessing with high predictive accuracy and automatic overfitting handling.
'''
model = ChatGroq(model="openai/gpt-oss-20b")
prompt1 = PromptTemplate.from_template(
    "generate me short notes of the given text \n {text}"
)
prompt2 = PromptTemplate.from_template(
    "generate me a quiz for the given text \n {text}"
)
prompt3 = PromptTemplate.from_template(
    "merge given notes and quiz into a single document \n notes -> {notes} \n quiz-> {quiz} "
)
parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz' : prompt2 | model | parser
})
merge_chain = prompt3 | model | parser
chain = parallel_chain | merge_chain
result = chain.invoke({
    'text':text
})
print(result)
chain.get_graph().print_ascii()