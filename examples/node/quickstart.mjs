/**
 * Node.js OpenAI SDK quickstart for Wanyra API (https://api.star1age.cn/v1).
 * Install: npm install openai
 * Run:     STAR1AGE_API_KEY="sk-..." node examples/node/quickstart.mjs
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.STAR1AGE_API_KEY,
  baseURL: "https://api.star1age.cn/v1",
});

async function main() {
  const models = await client.models.list();
  console.log(`Available GA models: ${models.data.length}`);

  const completion = await client.chat.completions.create({
    model: "star1age-gpt-6.2-sol",
    messages: [{ role: "user", content: "Reply with a one-sentence hello from Wanyra API." }],
  });
  console.log(completion.choices[0]?.message?.content);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
