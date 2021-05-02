from .run_model import runModel

class what2EatService:
    def saveCustomerRating(self, userRating):
        print("called saveCutomerRating")
        saveRating = runModel()
        saveRating.saveCustomerRating(userRating)

    def getRecommendationList(self, choice):
        print("called getRecommendationList")
        modelService = runModel()
        recommended_recipes = modelService.getRecommendedRecipes(choice)
        return recommended_recipes



