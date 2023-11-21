import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Logger } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.enableShutdownHooks();

  const mongoURI = process.env.MONGO_URI || 'mongodb://localhost:27017/user-crud';
  await app.listen(3000);

  Logger.log(`Application is running on: ${await app.getUrl()}`);


  // vamos simular que um erro aleatorio aconteceu
  // setTimeout(() => {
  //   process.exit(1);
  // }, Math.random() * 1e4); // 10.000
}

bootstrap();
