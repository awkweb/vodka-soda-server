export default {
  Query: {
    user: (parent, { username }, { models }) =>
      models.User.findOne({
        where: { username },
      }),
    users: (parent, args, { models }) => models.User.findAll(),
  },
  Mutation: {
    createUser: (parent, { input }, { models }) => models.User.create(input),
    updateUser: (parent, { id, input }, { models }) =>
      models.User
        .update({ ...input }, { where: { id } })
        .then(() => models.User.findOne({ where: { id } })),
    deleteUser: (parent, { id }, { models }) =>
      models.User.destroy({
        where: { id },
      }),
  },
};
