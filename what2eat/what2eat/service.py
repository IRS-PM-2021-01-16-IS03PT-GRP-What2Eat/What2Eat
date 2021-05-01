from .run_model import runModel

class what2EatService:
    def saveCutomerRating(self, userRating):
        print("called saveCutomerRating")
        saveRating = runModel()
        saveRating.saveCustomerRating(userRating)

    def getRecommendationList(self, choice):
        print("called getRecommendationList")
        modelService = runModel()
        modelService.getRecommendedRecipes(choice)



