import { Dialog, Transition } from '@headlessui/react'
import { Fragment, useState } from 'react'
import { LockClosedIcon } from '@heroicons/react/20/solid'
import {X} from 'lucide-react';
import Link from 'next/link';
import Image from 'next/image';




const Signin = () => {
    let [isOpen, setIsOpen] = useState(false)

    const closeModal = () => {
        setIsOpen(false)
    }

    const openModal = () => {
        setIsOpen(true)
    }

    return (
        <>
            <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0 bg">
                <div className='hidden md:block'>
                    <button type="button" className='flex justify-end text-xl font-medium bg-dark text-pink py-4 px-4 lg:px-8 navbutton rounded-full hover:text-white sign' onClick={openModal}>
                        Se connecter
                    </button>
                </div>
            </div>

            <Transition appear show={isOpen} as={Fragment}>
                <Dialog as="div" className="" onClose={closeModal}>
                    
                    <div className="fixed inset-0 overflow-y-auto">
                        <div className="flex min-h-full items-center justify-center p-4 text-center">
                            <Transition.Child
                                as={Fragment}
                                enter="ease-out duration-300"
                                enterFrom="opacity-0 scale-95"
                                enterTo="opacity-100 scale-100"
                                leave="ease-in duration-200"
                                leaveFrom="opacity-100 scale-100"
                                leaveTo="opacity-0 scale-95"
                            >
                                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl  p-6 text-left align-middle  transition-all">
                       

                                 <div className="min-h-screen  py-6 flex flex-col justify-center sm:py-12">
                                     <div style={{ display: 'flex', justifyContent: 'flex-end' }} className="inline-flex justify-center rounded-md border border-transparent px-4 py-2 text-sm font-medium text-blue-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 cursor-pointer"
                                                                    onClick={closeModal}>
                                            <X />
                                     </div>
                                  <div className="relative py-3 sm:max-w-xl sm:mx-auto">
                                    <div className="absolute inset-0 bg-gradient-to-r from-cyan-400 to-sky-500 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:rounded-3xl w-600"></div>
                                    <div className="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
                                      <div className="max-w-md mx-auto">
                                        <div>
                                          <h1 className="text-2xl font-semibold">Login</h1>
                                        </div>
                                        <div className="divide-y divide-gray-200">
                                          <div className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                                            <div className="relative">
                                              <input
                                                autoComplete="off"
                                                id="email"
                                                name="email"
                                                type="text"
                                                className="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:borer-rose-600"
                                                placeholder="Email address"
                                              />
                                              <label
                                                htmlFor="email"
                                                className="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
                                              >
                                                Adresse email
                                              </label>
                                            </div>
                                            <div className="relative">
                                              <input
                                                autoComplete="off"
                                                id="password"
                                                name="password"
                                                type="password"
                                                className="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:borer-rose-600"
                                                placeholder="Password"
                                              />
                                              <label
                                                htmlFor="password"
                                                className="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
                                              >
                                                Mot de passe
                                              </label>
                                            </div>
                                            <div className="relative">
                                              <button className="bg-cyan-500 text-white rounded-md px-2 py-1">
                                                Valider
                                              </button>
                                            </div>
                                          </div>
                                        </div>
                                      </div>
                                      <div className="w-full flex justify-center">
                                        <button className="flex items-center bg-white border border-gray-300 rounded-lg shadow-md px-6 py-2 text-sm font-medium text-gray-800 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                                          <svg
                                            className="h-6 w-6 mr-2"
                                            xmlns="http://www.w3.org/2000/svg"
                                            xmlnsXlink="http://www.w3.org/1999/xlink"
                                            width="800px"
                                            height="800px"
                                            viewBox="-0.5 0 48 48"
                                            version="1.1"
                                          >
                                            {" "}
                                            <title>Google-color</title> <desc>Created with Sketch.</desc>{" "}
                                            <defs> </defs>{" "}
                                            <g
                                              id="Icons"
                                              stroke="none"
                                              strokeWidth={1}
                                              fill="none"
                                              fillRule="evenodd"
                                            >
                                              {" "}
                                              <g id="Color-" transform="translate(-401.000000, -860.000000)">
                                                {" "}
                                                <g id="Google" transform="translate(401.000000, 860.000000)">
                                                  {" "}
                                                  <path
                                                    d="M9.82727273,24 C9.82727273,22.4757333 10.0804318,21.0144 10.5322727,19.6437333 L2.62345455,13.6042667 C1.08206818,16.7338667 0.213636364,20.2602667 0.213636364,24 C0.213636364,27.7365333 1.081,31.2608 2.62025,34.3882667 L10.5247955,28.3370667 C10.0772273,26.9728 9.82727273,25.5168 9.82727273,24"
                                                    id="Fill-1"
                                                    fill="#FBBC05"
                                                  >
                                                    {" "}
                                                  </path>{" "}
                                                  <path
                                                    d="M23.7136364,10.1333333 C27.025,10.1333333 30.0159091,11.3066667 32.3659091,13.2266667 L39.2022727,6.4 C35.0363636,2.77333333 29.6954545,0.533333333 23.7136364,0.533333333 C14.4268636,0.533333333 6.44540909,5.84426667 2.62345455,13.6042667 L10.5322727,19.6437333 C12.3545909,14.112 17.5491591,10.1333333 23.7136364,10.1333333"
                                                    id="Fill-2"
                                                    fill="#EB4335"
                                                  >
                                                    {" "}
                                                  </path>{" "}
                                                  <path
                                                    d="M23.7136364,37.8666667 C17.5491591,37.8666667 12.3545909,33.888 10.5322727,28.3562667 L2.62345455,34.3946667 C6.44540909,42.1557333 14.4268636,47.4666667 23.7136364,47.4666667 C29.4455,47.4666667 34.9177955,45.4314667 39.0249545,41.6181333 L31.5177727,35.8144 C29.3995682,37.1488 26.7323182,37.8666667 23.7136364,37.8666667"
                                                    id="Fill-3"
                                                    fill="#34A853"
                                                  >
                                                    {" "}
                                                  </path>{" "}
                                                  <path
                                                    d="M46.1454545,24 C46.1454545,22.6133333 45.9318182,21.12 45.6113636,19.7333333 L23.7136364,19.7333333 L23.7136364,28.8 L36.3181818,28.8 C35.6879545,31.8912 33.9724545,34.2677333 31.5177727,35.8144 L39.0249545,41.6181333 C43.3393409,37.6138667 46.1454545,31.6490667 46.1454545,24"
                                                    id="Fill-4"
                                                    fill="#4285F4"
                                                  >
                                                    {" "}
                                                  </path>{" "}
                                                </g>{" "}
                                              </g>{" "}
                                            </g>{" "}
                                          </svg>
                                          <span>Se connecter avec google</span>
                                        </button>
                                        
                                 
                                      </div>
                                         <div className="mt-4 flex justify-end "style={{marginBottom:'15%',marginTop:'15%'}}>
                                        <Link href='/Login'>
                                               <div className="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2">
Inscrivez-vous
                                               </div>
                                          
                                           
                                        
                                      </Link>
                                    </div>
                                    </div>
                                  </div>
                                    </div>


                                </Dialog.Panel>
                            </Transition.Child>
                        </div>
                    </div>
                </Dialog>
            </Transition>
        </>
    )
}

export default Signin;
