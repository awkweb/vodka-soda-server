export default ` 
  input UserInput {
    email: String!
    facebookAccessToken: String!
    facebookId: Int!
    gender: String
    name: String
  }
  
  type User {
    id: ID!
    email: String!
    facebookAccessToken: String!
    facebookId: Int!
    gender: String!
    name: String!
    createdAt: String!
    updatedAt: String!
  }
  
  type Query {
    user(username: String!): User
    users: [User!]!
  }
  
  type Mutation {
    createUser(input: UserInput): User
    deleteUser(id: ID!): Int!
    updateUser(id: ID!, input: UserInput): User
  }
`;
