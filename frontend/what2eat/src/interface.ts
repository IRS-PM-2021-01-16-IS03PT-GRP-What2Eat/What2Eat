// export interface FoodAPI {
//     count: number;
//     next: string;
//     results: Results[];
//   }

export interface Food {
    recipe_id: string, 
    recipe_name: string, 
    ingredients: string,
    image_url: string,
    methods: string,
  }

  export interface FoodWithRating {
    recipe_id: string, 
    recipe_name: string, 
    ingredients: string,
    image_url: string,
    methods: string,
    rating: number
  }

  export interface FoodRating {
    id: string, 
    rating: number
  }

  export interface SubmitFoodRating {
    username: string,
    id: string, 
    rating: number
  }

  export interface Register {
    username: string, 
    password: string, 
    foodRatingList: Array<FoodRating>
  }
  
  
  