from .run_model import runModel

class what2EatService:
    # def saveCustomerRating(self, userRating):
    #     print("called saveCutomerRating")
    #     saveRating = runModel()
    #     saveRating.saveCustomerRating(userRating)

    def getRecommendationList(self, choice, ratings):
        print("called getRecommendationList")
        modelService = runModel()
        recommended_recipes = modelService.getRecommendedRecipes(choice, ratings)
        return recommended_recipes



