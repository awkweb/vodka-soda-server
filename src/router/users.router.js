import { Router } from 'express';
import { usersController } from '../controllers';

const router = new Router();

router.post('/users', usersController.logIn);
router.get('/users/:id', usersController.get);

export default router;
