const stripe = require('stripe')(process.env.STRIPE_KEY);

export default async function handler(req, res) {
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{ price: 'price_H5ggv97645', quantity: 1 }],
    mode: 'payment',
    success_url: 'https://chalamandra-onion-heuristic-b.vercel.app/success',
    cancel_url: 'https://chalamandra-onion-heuristic-b.vercel.app/cancel',
  });
  res.status(200).json({ url: session.url });
}
