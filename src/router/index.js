import { Router } from 'express';
import usersRouter from './users.router';

const router = new Router();

router.use(usersRouter);

export default router;
