// export interface FoodAPI {
//     count: number;
//     next: string;
//     results: Results[];
//   }

export interface Food {
    id: string, 
    title: string, 
    description: string, 
    ingredients: string,
    link: string,
    method: string,
    thumbnail: string
  }

  export interface FoodWithRating {
    id: string, 
    title: string, 
    description: string, 
    ingredients: string,
    link: string,
    method: string,
    thumbnail: string,
    rating: number
  }

  export interface FoodRating {
    id: string, 
    rating: number
  }

  export interface Register {
    username: string, 
    password: string, 
    foodRatingList: Array<FoodRating>
  }
  
  
  