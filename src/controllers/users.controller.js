import db from '../models';
const User = db.sequelize.models.User;

export default {
  logIn(req, res) {
    console.log('merp', req);
    const user = User.findOne({ where: { email: req.body.email || 'thom.meagher@gmail.com' } });
    if (user) {
      res.status(201).send(user);
    } else {
      return User
        .create({
          email: req.body.email,
          name: req.body.name,
          age: req.body.age,
          gender: req.body.gender,
        })
        .then(user => res.status(201).send(user))
        .catch(error => res.status(400).send(error));
    }
  },
  get(req, res) {
    return User
      .findOne({ where: { id: req.params.id } })
      .then(user => res.status(201).send(user))
      .catch(error => res.status(400).send(error));
  },
};
